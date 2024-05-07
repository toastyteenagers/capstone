#include <algorithm>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>

int main()
{
    std::ifstream fin("/home/team11/debug/voltage.txt");
    std::string buf;
    int ibuf = 0;
    double dbuf = 0;
    std::vector<double> v;
    while ( std::getline(fin, buf) )
    {
        ibuf = std::stoi(buf);
        dbuf = static_cast<double>(ibuf);
        v.push_back(dbuf);
    }
    fin.close();
    if ( !v.size() )
    {
        std::cerr << "No measurement taken. Exiting.\n";
        return 1;
    }
    double mean = 0;
    for (auto const& it : v)
    {
        mean += it;
    }
    mean /= v.size();
    double stdev = 0;
    for (auto const& it : v)
    {
        stdev += (it - mean) * (it - mean);
    }
    stdev /= v.size();
    stdev = sqrt(stdev);
    std::sort(v.begin(), v.end());
    int idx10, idx25, idx50, idx75, idx90;
    int split25, split50, split75;
    if (v.size() <= 3)
    {
        std::cerr << "Sample size is too small (must be at least 4)\n";
        return 1;
    }
    else
    {
        if (v.size() >= 10)
        {
            idx10 = v.size() / 10;
            idx90 = v.size() - idx10;
        }
        else
        {
            idx10 = idx90 = -1;
        }
        idx25 = (v.size() - 2) / 4;
        idx50 = (v.size() - 1) / 2;
        idx75 = (v.size() / 4) * 3 - 1 + (v.size() % 4);
        split25 = split75 = v.size() % 4 < 2;
        split50 = v.size() % 2 == 0;
    }
    int p10 = (idx10 == -1? -1 : v[idx10]);
    int p25 = (idx25 == -1? -1 : v[idx25] / (split25? 2 : 1) + (split25? v[idx25 + 1] / 2 : 0) );
    int p50 = v[idx50] / (split50? 2 : 1) + (split50? v[idx50 + 1] / 2 : 0);
    int p75 = (idx75 == -1? -1 : v[idx75] / (split75? 2 : 1) + (split75? v[idx75 + 1] / 2 : 0) );
    int p90 = (idx90 == -1? -1 : v[idx90]);
    int loOutlier = 0;
    int hiOutlier = 0;
    int IQR = p75 - p25;
    for (auto const& it : v)
    {
        if (it < static_cast<double>(p25) - 1.5 * IQR)
        {
            ++loOutlier;
        }
        if (it > static_cast<double>(p75) + 1.5 * IQR)
        {
            ++hiOutlier;
        }
    }
    std::cout << "      mean voltage: " << mean << " mV\n";
    std::cout << "standard deviation: " << stdev << " mV\n";
    std::string str10 = (p10 == -1? "----" : std::to_string(p10)) + "|";
    std::string str25 = (p25 == -1? "----" : std::to_string(p25)) + "|";
    std::string str50 = std::to_string(p50) + "|";
    std::string str75 = (p75 == -1? "----" : std::to_string(p75)) + "|";
    std::string str90 = (p90 == -1? "----" : std::to_string(p90)) + "|";
    std::cout << v.front() << "|" << str10 << str25 << str50 << str75 << str90 << v.back() << "\n";
    std::cout << "min.|10%e|25%e|med.|75%e|90%e|max.\n";
    std::cout << " low outliers: " << loOutlier << "/" << v.size() << "\n";
    std::cout << "high outliers: " << hiOutlier << "/" << v.size() << "\n";
    return 0;
}

