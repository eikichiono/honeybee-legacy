# By Mostapha Sadeghipour Roudsari
# Sadeghipour@gmail.com
# Honeybee started by Mostapha Sadeghipour Roudsari is licensed
# under a Creative Commons Attribution-ShareAlike 3.0 Unported License.

"""
EnergyPlus Shadow Parameters
-
Provided by Honeybee 0.0.53

    Args:
        calculationMethod_:...
        frequency_: ...
        maximumFigure_: ...
    Returns:
        shadowPar:...
"""

ghenv.Component.Name = "Honeybee_ShadowPar"
ghenv.Component.NickName = 'shadowPar'
ghenv.Component.Message = 'VER 0.0.53\nMAY_12_2014'
ghenv.Component.Category = "Honeybee"
ghenv.Component.SubCategory = "09 | Energy | Energy"
try: ghenv.Component.AdditionalHelpFromDocStrings = "3"
except: pass


def main(calculationMethod, frequency, maximumFigure):
    # I will add check for inputs later
    if calculationMethod== None:
        calculationMethod = "AverageOverDaysInFrequency"
        #"TimestepFrequency"
    if frequency == None: frequency =  30
    if maximumFigure == None: maximumFigure = 3000

    return calculationMethod, frequency, maximumFigure
    

shadowPar = main(calculationMethod_, frequency_, maximumFigure_)