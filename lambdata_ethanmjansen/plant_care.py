'''
Class to represent plant care.
'''


class Plant_Care:
    '''
    General representation of abstract plant care.
    '''
    def __init__(self,
                 times_monthly=2,
                 plant_type='Cacti',
                 soil_moisutre='Arid'):
        self.times_monthly = times_monthly
        self.plant_type = plant_type
        self.soil_moisture = soil_moisutre

    def print_times_monthly(self):
        '''
        Print how many times you should water monthly.
        '''
        print('water {} times monthly'.format(self.times_monthly))
        