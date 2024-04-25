# from the information found in this paper: https://www.researchgate.net/figure/Distribution-of-average-daily-resting-heart-rates-The-average-daily-RHR-for-57-836_fig2_339061433

import UserFields

mean = 65.5
std_dev = 3.10
allowable_deviation = 3

#return true if the user is 3+ deviatons away from the mean set from their resting rate.
def analyze(userField,observedHR):
    std_deviations_away = abs(observedHR-userField.get_rhr()) / std_dev
    return std_deviations_away > allowable_deviation

# this class will analyze the users' resting heart rate by using a statistical model derived
