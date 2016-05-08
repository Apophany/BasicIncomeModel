from basic_income_assumptions import *
from scipy.stats import *

NON_WORKERS = NUM_OF_ADULTS - LABOUR_FORCE - DISABLED_ADULTS


def basic_income_cost_benefit():
    direct_cost = NUM_OF_ADULTS * BASIC_INCOME

    # Admin costs here are modelled as being either
    # as small as $0 or as large as $500 and so are
    # modelled as a normal distribution, mean 250, sigma 75
    administrative_costs_per_person = norm(250, 75)
    adminstrative_cost = administrative_costs_per_person.rvs() * NUM_OF_ADULTS

    return (direct_cost +
            adminstrative_cost +
            cost_benefit_labour_disincentive() +
            jk_rowling_effect(NON_WORKERS))


# Modelled by the fact that non-working adults may
# increase or decrease by +15/-5% and that these
# adults will have a wage modelled by a normal distribution
# centered on $10/hour
def cost_benefit_labour_disincentive():
    non_worker_multipler = uniform(-0.05, 0.15)
    marginal_worker_hourly_productivity = norm(10, 1)

    return (-1 * NON_WORKERS * non_worker_multipler.rvs() *
            (WEEKS_PER_YEAR * HOURS_PER_WEEK * marginal_worker_hourly_productivity.rvs()))


# This is the propensity for otherwise
# unemployed individuals to create wealth
def jk_rowling_effect(num_non_workers):
    num_of_jk_rowlings = binom(num_non_workers, 1e-7).rvs()
    return num_of_jk_rowlings * 1e9
