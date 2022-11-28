ID Number:205933
Name:De Guzman, Luis Sebastian V.
Year and Course:2 BS ITE

def savings(gross_pay, tax_rate, expenses):
    '''Savings.
    2 points.
    This function calculates the money remaining
        for an employee after taxes and expenses.
    
    To get the take-home pay of an employee, we will
        follow the following process:
        1. Apply the tax rate to the gross pay of the employee; round down
        2. Subtract the expenses from the after-tax pay of the employee
    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos
    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.


# In[1]:

def savings(gross_pay, tax_rate, expenses):
    print("grosspay:")
    gross_pay = input()
    gross_pay = int(gross_pay)

    print("expenses:")
    expenses = input()
    expenses = int(expenses)

    print("taxrate:")
    tax_rate = input()
    tax_rate = float(tax_rate)

    netPay = tax_rate * gross_pay
    return netPay - expenses

def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.
    2 points.
    This function calculates how much material input will be wasted
        after running a certain number of jobs that consume
        a set amount of material.
    To get the waste of a set of jobs:
        1. Multiply the number of jobs by the material consumption per job.
        2. Subtract the total material consumed from the total material available.
    The users of this function also want you to format the output as a string, annotated with the
        units in which the material is expressed. Do not add a space between the number and the unit.
    Parameters
    ----------
    total_material: int
        the total material available
    material_units: str
        the units used to express a quantity of the material (e.g., "kg", "L", etc.)
    num_jobs: int
        the number of jobs to run
    job_consumption: int
        the amount of material consumed per job
    Returns
    -------
    str
        the amount of remaining material expressed with its unit (e.g., "10kg").
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.


# In[13]:

def material_waste(total_material, material_units, num_jobs, job_consumption):
    print("num jobs:")
    num_jobs = input()
    num_jobs = int(num_jobs)

    print("material consumption:")
    job_consumption = input()
    job_consumption = int(job_consumption)

    print("total material:")
    total_material = input()
    total_material = int(total_material)

    print("material units:")
    material_units = input()

    waste_set = num_jobs * job_consumption
    waste_set2 = total_material - waste_set
    return waste_set2 + material_units
    
    # In[ ]:


def interest(principal, rate, periods):
    '''Interest.
    3 points.
    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.
    To calculate simple interest, simply multiply the principal to the quantity (rate * time). 
        Add this amount to the principal to get the final value.
    Round down the final amount.
    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested
    Returns
    -------
    int
        the final value of the investment
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.


# In[18]:

def interest(principal, rate, periods):
    print("Principal:")
    principal = input()
    principal = int(principal)

    print("material consumption:")
    rate = input()
    rate = int(rate)

    print("total material:")
    periods = input()
    periods = int(periods)

    simp_int = principal + (principal * (rate*periods))
    return simp_int

# In[ ]:


def body_mass_index(weight, height):
    '''Body Mass Index.
    3 points.
    This function calculates the body mass index (BMI) of a person
        given their weight and height.
    The formula for BMI is: kg / (m ^ 2)
        (i.e., kilograms over meters squared)
    Unfortunately, the users of this function use the imperial system.
        You will need to first convert their arguments to the metric system.
    
    Parameters
    ----------
    weight: float
        the weight of the person, in pounds
    height: list
        the height of the person, expressed as a list of two integers.
        the first integer is the foot component of their height.
        the second integer is the inches component of their height.
        for example, 5'10" would be passed as [5, 10].
    Returns
    -------
    float
        the BMI of the person.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.


# In[24]:

def body_mass_index(weight, height):
    print("weight:")
    weight = input()
    weight = int(weight)

    print("height:")
    height = input()
    height = int(height)

    bmiValue = weight / (pow(2,height)*2)
    return bmiValue

# In[ ]:

