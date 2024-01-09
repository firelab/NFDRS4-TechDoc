# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 14:32:41 2022

@author: mjolly

"""

from math import exp
def pow(base, expn):
    return base ** expn



## \fn fToC Converts Fahrenheit to Celcius
## \param f Temperature in deg F
## \return c Temperature in deg C
def fToc(f):
    return (f -32) * 5/9

## \fn cTof Converts Celcius to Fahrenheit
## \param c Temperature in deg C
## \return f Temperature in deg F
def cTof(c):
    return (c * 9/5) + 32

## \class USNFDRSFuelModel
## \brief US NFDRS Fuel Model Class
class USNFDRSFuelModel:
    CTA = 0.046
    SG1 = 2000	## \var SG1 1hr Surface Area to Volume Ratio
    SG10 = 109	## 10hr Surface Area to Volume Ratio
    SG100 = 30	## 100hr Surface Area to Volume Ratio
    SG1000 = 8	## 1000hr Surface Area to Volume Ratio
    SGWOOD = 1	## Wood Surface Area to Volume Ratio
    SGHERB = 1	## Herbaceous Surface Area to Volume Ratio
    L1 = 1		## 1hr fuel loading
    L10 = 1		## 10hr fuel loading
    L100 = 1	## 100hr fuel loading
    L1000 = 1	## 1000hr fuel loading
    LWOOD = 1	## Woody fuel loading
    LHERB = 1	## Herbaceous fuel loading
    DEPTH = 1	## Fuel bed depth
    MXD = 15	## Dead fuel moisture of extinction
    DROUGHT = 0 ## Drought fuel loading
    HD = 8000
    SCM = 301
    WNDFC = 0.6
    FuelModel = ""
    FMCode = ""
    W1 = L1 * CTA
    W1P = 0.0
    W10 = L10 * CTA
    W100 = L100 * CTA
    W1000 = L1000 * CTA
    WWOOD = LWOOD * CTA
    WHERB = LHERB * CTA
    WHERBP = 0.0

    ## \fn __init__(self,FMCode)
    ## \param FMCode Fuel Model Code (A = Grass, F = Brush, G = Timber Understory, Anything else is set to the Slash model)
    def __init__(self,FMCode):
        self.FMCode = FMCode.upper()

        if self.FMCode == "A":	#Grass fuel model
            self.SG1 = 3000
            self.SG10 = 0
            self.SG100 = 0
            self.SG1000 = 0
            self.SGWOOD = 0
            self.SGHERB = 3000
            self.L1 = .2
            self.L10 = 0
            self.L100 = 0
            self.L1000 = 0
            self.LWOOD = 0
            self.LHERB = .3
            self.DEPTH = .8
            self.MXD = 15
            self.HD = 8000
            self.SCM = 301
            self.WNDFC = 0.6
        elif self.FMCode == "B":
            self.SG1 = 700
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGWOOD = 1250
            self.SGHERB = 3000
            self.L1 = 3.5
            self.L10 = 4
            self.L100 = 0.5
            self.L1000 = 0
            self.LWOOD = 11.5
            self.LHERB = 0
            self.DEPTH = 4.5
            self.MXD = 15
            self.HD = 9500
            self.SCM = 58
            self.WNDFC = 0.5
        elif self.FMCode == "C":
            self.SG1 = 2000
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGWOOD = 1500
            self.SGHERB = 2500
            self.L1 = 0.4
            self.L10 = 1
            self.L100 = 0
            self.L1000 = 0
            self.LWOOD = 0.5
            self.LHERB = 0.8
            self.DEPTH = 0.75
            self.MXD = 20
            self.HD = 8000
            self.SCM = 32
            self.WNDFC = 0.5
        elif self.FMCode == "D":
            self.SG1 = 1250
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGWOOD = 1500
            self.SGHERB = 1500
            self.L1 = 2
            self.L10 = 1
            self.L100 = 0
            self.L1000 = 0
            self.LWOOD = 3
            self.LHERB = 0.75
            self.DEPTH = 2
            self.MXD = 30
            self.HD = 9000
            self.SCM = 68
            self.WNDFC = 0.4
        elif self.FMCode == "E":
            self.SG1 = 2000
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGWOOD = 1500
            self.SGHERB = 2000
            self.L1 = 1.5
            self.L10 = 0.5
            self.L100 = 0.25
            self.L1000 = 0
            self.LWOOD = 0.5
            self.LHERB = 0.5
            self.DEPTH = 0.4
            self.MXD = 25
            self.HD = 8000
            self.SCM = 25
            self.WNDFC = 0.4
        elif self.FMCode == "F":	# Brush fuel model
            self.SG1 = 700
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 0
            self.SGWOOD = 1250
            self.SGHERB = 0
            self.L1 = 2.5
            self.L10 = 2
            self.L100 = 1.5
            self.L1000 = 0
            self.LWOOD = 9
            self.LHERB = 0
            self.DEPTH = 4.5
            self.MXD = 15
            self.HD = 9500
            self.SCM = 24
            self.WNDFC = 0.5
        elif self.FMCode == "G":	# Timber understory fuel model
            self.SG1 = 2000
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGWOOD = 1500
            self.SGHERB = 2000
            self.L1 = 2.5
            self.L10 = 2
            self.L100 = 5
            self.L1000 = 12
            self.LWOOD = .5
            self.LHERB = .5
            self.DEPTH = 1
            self.MXD = 25
            self.HD = 8000
            self.SCM = 30
            self.WNDFC = 0.4
        elif self.FMCode == "H":	# Timber understory fuel model
            self.L1 = 1.5
            self.L10 = 1
            self.L100 = 2
            self.L1000 = 2
            self.LHERB = .5
            self.LWOOD = .5
            self.SG1 = 2000
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGHERB = 2000
            self.SGWOOD = 1500
            self.HD = 8000
            self.MXD = 20
            self.DEPTH = 0.3
            self.WNDFC = 0.4
            self.SCM = 8
        elif self.FMCode == "I":	# Timber understory fuel model
            self.L1 = 12
            self.L10 = 12
            self.L100 = 10
            self.L1000 = 12
            self.LHERB = 0
            self.LWOOD = 0
            self.SG1 = 1500
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGHERB = 2000
            self.SGWOOD = 1500
            self.HD = 8000
            self.MXD = 25
            self.DEPTH = 2
            self.WNDFC = 0.5
            self.SCM = 65
        elif self.FMCode == "J":	# Timber understory fuel model
            self.L1 = 7
            self.L10 = 7
            self.L100 = 6
            self.L1000 = 5.5
            self.LHERB = 0
            self.LWOOD = 0
            self.SG1 = 1500
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGHERB = 2000
            self.SGWOOD = 1500
            self.HD = 8000
            self.MXD = 25
            self.DEPTH = 1.3
            self.WNDFC = 0.5
            self.SCM = 44
        elif self.FMCode == "K":	# Timber understory fuel model
            self.L1 = 2.5
            self.L10 = 2.5
            self.L100 = 2
            self.L1000 = 2.5
            self.LHERB = 0
            self.LWOOD = 0
            self.SG1 = 1500
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGHERB = 2000
            self.SGWOOD = 1500
            self.HD = 8000
            self.MXD = 25
            self.DEPTH = 0.6
            self.WNDFC = 0.5
            self.SCM = 23
        elif self.FMCode == "L":	# Timber understory fuel model
            self.L1 = 0.25
            self.L10 = 0
            self.L100 = 0
            self.L1000 = 0
            self.LHERB = 0.5
            self.LWOOD = 0
            self.SG1 = 2000
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGHERB = 2000
            self.SGWOOD = 1500
            self.HD = 8000
            self.MXD = 15
            self.DEPTH = 1
            self.WNDFC = 0.6
            self.SCM = 178
        elif self.FMCode == "N":	# Timber understory fuel model
            self.L1 = 1.5
            self.L10 = 1.5
            self.L100 = 0
            self.L1000 = 0
            self.LHERB = 0
            self.LWOOD = 2
            self.SG1 = 1600
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGHERB = 2000
            self.SGWOOD = 1500
            self.HD = 8700
            self.MXD = 25
            self.DEPTH = 3
            self.WNDFC = 0.6
            self.SCM = 167
        elif self.FMCode == "O":	# Timber understory fuel model
            self.L1 = 2
            self.L10 = 3
            self.L100 = 3
            self.L1000 = 2
            self.LHERB = 0
            self.LWOOD = 7
            self.SG1 = 1500
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGHERB = 1500
            self.SGWOOD = 1500
            self.HD = 9000
            self.MXD = 30
            self.DEPTH = 4
            self.WNDFC = 0.5
            self.SCM = 99
        elif self.FMCode == "P":	# Timber understory fuel model
            self.L1 = 1
            self.L10 = 1
            self.L100 = 0.5
            self.L1000 = 2
            self.LHERB = 0.5
            self.LWOOD = 0.5
            self.SG1 = 1750
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGHERB = 2000
            self.SGWOOD = 1500
            self.HD = 8000
            self.MXD = 30
            self.DEPTH = 0.4
            self.WNDFC = 0.4
            self.SCM = 14
        elif self.FMCode == "Q":	# Timber understory fuel model
            self.L1 = 2
            self.L10 = 2.5
            self.L100 = 2
            self.L1000 = 1
            self.LHERB = 0.5
            self.LWOOD = 4
            self.SG1 = 1500
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGHERB = 1500
            self.SGWOOD = 1200
            self.HD = 8000
            self.MXD = 25
            self.DEPTH = 3
            self.WNDFC = 0.4
            self.SCM = 59
        elif self.FMCode == "R":	# Timber understory fuel model
            self.L1 = 0.5
            self.L10 = 0.5
            self.L100 = 0.5
            self.L1000 = 0
            self.LHERB = 0.5
            self.LWOOD = 0.5
            self.SG1 = 1500
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGHERB = 2000
            self.SGWOOD = 1500
            self.HD = 8000
            self.MXD = 25
            self.DEPTH = 0.25
            self.WNDFC = 0.4
            self.SCM = 6
        elif self.FMCode == "S":	# Timber understory fuel model
            self.L1 = 0.5
            self.L10 = 0.5
            self.L100 = 0.5
            self.L1000 = 0.5
            self.LHERB = 0.5
            self.LWOOD = 0.5
            self.SG1 = 1500
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGHERB = 1500
            self.SGWOOD = 1200
            self.HD = 8000
            self.MXD = 25
            self.DEPTH = 0.4
            self.WNDFC = 0.6
            self.SCM = 17
        elif self.FMCode == "T":	# Timber understory fuel model
            self.L1 = 1
            self.L10 = 0.5
            self.L100 = 0
            self.L1000 = 0
            self.LHERB = 0.5
            self.LWOOD = 2.5
            self.SG1 = 2500
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGHERB = 2000
            self.SGWOOD = 1500
            self.HD = 8000
            self.MXD = 15
            self.DEPTH = 1.25
            self.WNDFC = 0.6
            self.SCM = 96
        elif self.FMCode == "U":	# Western Pines
            self.L1 = 1.5
            self.L10 = 1.5
            self.L100 = 1
            self.L1000 = 0
            self.LHERB = 0.5
            self.LWOOD = 0.5
            self.SG1 = 1750
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGHERB = 2000
            self.SGWOOD = 1500
            self.HD = 8000
            self.MXD = 20
            self.DEPTH = 0.5
            self.WNDFC = 0.4
            self.SCM = 16
        
        elif self.FMCode == "V":  # Grass
            self.SG1 = 2000
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGWOOD = 1500
            self.SGHERB = 2000
            self.L1 = 0.1
            self.L10 = 0.0
            self.L100 = 0.0
            self.L1000 = 0.0
            self.LWOOD = 0.0
            self.LHERB = 1.0
            self.DEPTH = 1
            self.MXD = 15
            self.HD = 8000
            self.SCM = 108
            self.WNDFC = 0.6
            self.DROUGHT = 0

        elif self.FMCode == "W":  # Grass
            
            self.SG1 = 2000
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGWOOD = 1500
            self.SGHERB = 2000
            self.L1 = 0.5
            self.L10 = 0.5
            self.L100 = 0.0
            self.L1000 = 0.0
            self.LWOOD = 1.0
            self.LHERB = 0.6
            self.DEPTH = 1.5
            self.MXD = 15
            self.HD = 8000
            self.SCM = 62
            self.WNDFC = 0.4
            self.DROUGHT = 1
        elif self.FMCode == "X":  # Grass
            print("X")
            self.SG1 = 2000
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGWOOD = 1500
            self.SGHERB = 2000
            self.L1 = 4.5
            self.L10 = 2.45
            self.L100 = 0.0
            self.L1000 = 0.0
            self.LWOOD = 7.0
            self.LHERB = 1.55
            self.DEPTH = 4.4
            self.MXD = 25
            self.HD = 8000
            self.SCM = 104
            self.WNDFC = 0.4
            self.DROUGHT = 2.5


        elif self.FMCode == "Y":  # Timber understory fuel model
            self.SG1 = 2000
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGWOOD = 1500
            self.SGHERB = 2000
            self.L1 = 2.5
            self.L10 = 2.2
            self.L100 = 3.6
            self.L1000 = 10.16
            self.LWOOD = 0
            self.LHERB = 0
            self.DEPTH = 0.6
            self.MXD = 25
            self.HD = 8000
            self.SCM = 5
            self.WNDFC = 0.2
            self.DROUGHT = 5
 
        elif self.FMCode == "Z":  # Grass
            self.SG1 = 2000
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGWOOD = 1500
            self.SGHERB = 2000
            self.L1 = 4.5
            self.L10 = 4.25
            self.L100 = 4.0
            self.L1000 = 4.0
            self.LWOOD = 0.0
            self.LHERB = 0.0
            self.DEPTH = 1.5
            self.MXD = 25
            self.HD = 8000
            self.SCM = 19
            self.WNDFC = 0.4
            self.DROUGHT = 7
        else:	# Assign the Slash Fuel Model Parameters

            self.SG1 = 1500
            self.SG10 = 109
            self.SG100 = 30
            self.SG1000 = 8
            self.SGWOOD = 0
            self.SGHERB = 0
            self.L1 = 7
            self.L10 = 7
            self.L100 = 6
            self.L1000 = 5.5
            self.LWOOD = 0
            self.LHERB = 0
            self.DEPTH = 1.3
            self.MXD = 25
            self.HD = 8000
            self.SCM = 44
            self.WNDFC = 0.5

        if (self.SG1 <= 0):
            self.SG1 = 2000
        if (self.SG10 <= 0):
            self.SG10 = 109
        if (self.SG100 <=0 ):
            self.SG100 = 30
        if (self.SG1000 <= 0):
            self.SG1000 = 8
        if (self.SGWOOD <= 0):
            self.SGWOOD = 1
        if (self.SGHERB <= 0):
            self.SGHERB = 1
        self.W1 = self.L1 * self.CTA
        self.W10 = self.L10 * self.CTA
        self.W100 = self.L100 * self.CTA
        self.W1000 = self.L1000 * self.CTA
        self.WWOOD = self.LWOOD * self.CTA
        self.WHERB = self.LHERB * self.CTA
    
class FuelMoisture:
    MC1 = 4
    MC10 = 5
    MC100 = 6
    MC1000 = 7
    MCHERB = 60
    MCWOOD = 90


def iCalcIndexes (FM,MC,iWS, iSlopeCls,fGSI, KBDI,FuelTemperature):

    CTA = 0.0459137
    KBDIThreshold = 100
    STD = .0555
    STL = .0555
    RHOD = 32
    RHOL = 32
    ETASD = 0.4173969
    ETASL = 0.4173969
       
    # Fuel Model Y Parameters
    SG1 = FM.SG1
    SG10 = FM.SG10
    SG100 = FM.SG100
    SG1000 = FM.SG1000
    SGWOOD = FM.SGWOOD
    SGHERB = FM.SGHERB
    L1 = FM.L1
    L10 = FM.L10
    L100 = FM.L100
    L1000 = FM.L1000
    LWOOD = FM.LWOOD
    LHERB = FM.LHERB
    DEPTH = FM.DEPTH
    MXD = FM.MXD
    HD = FM.HD
    SCM = FM.SCM
    WNDFC = FM.WNDFC
    LDROUGHT = FM.DROUGHT
    
    # Fuel Moistures
    MC1 = MC.MC1
    MC10 = MC.MC10
    MC100 = MC.MC100
    MC1000 = MC.MC1000
    MCHERB = MC.MCHERB
    MCWOOD = MC.MCWOOD
        
    W1 = L1 * CTA
    W10 = L10 * CTA
    W100 = L100 * CTA
    W1000 = L1000 * CTA
    WWOOD = LWOOD * CTA
    WHERB = LHERB * CTA
    WWOOD = LWOOD * CTA
    WDROUGHT = LDROUGHT * CTA
    fDEPTH = DEPTH
   
    if (KBDI > KBDIThreshold ):
        WTOTD = W1 + W10 + W100
        WTOTL = WHERB + WWOOD
        WTOT = WTOTD + WTOTL
        PackingRatio = WTOT / fDEPTH
        if (PackingRatio == 0):
            PackingRatio = 1.0
        WTOTD = WTOTD + W1000
        
        DroughtUnit = WDROUGHT / (800.0 - KBDIThreshold)

        W1 = W1 + (W1 / WTOTD) * (KBDI - 100) * DroughtUnit
        W10 = W10 + (W10 / WTOTD) * (KBDI - 100) * DroughtUnit
        W100 = W100 + (W100 / WTOTD) * (KBDI - 100) * DroughtUnit
        W1000 = W1000 + (W1000 / WTOTD) * (KBDI - 100) * DroughtUnit
        WTOT = W1 + W10 + W100 + W1000 + WTOTL
        fDEPTH = (WTOT - W1000) / PackingRatio
    
    fctCur = 1.33 - .0111 * MCHERB
    if (fctCur < 0):
        fctCur = 0.0
    if (fctCur > 1):
        fctCur = 1.0;
    W1P = W1 + WHERB * fctCur
    WHERBP = WHERB * (1 - fctCur)
    


    WTOTD = W1P + W10 + W100 + W1000					# Total Dead Fuel Loading
    
    WTOTL = WHERBP + WWOOD								# Total Live Fuel Loading
    WTOT = WTOTD + WTOTL								# Total Fuel Loading
   
    W1N = W1P * (1.0 - STD)							# Net 1hr Fuel Loading
    W10N = W10 * (1.0 - STD)							# Net 10hr Fuel Loading
    W100N = W100 * (1.0 - STD)							# Net 100hr Fuel Loading
    WHERBN = WHERBP * (1.0 - STL)						# Net Herbaceous Fuel Loading
    WWOODN = WWOOD * (1.0 - STL)						# Net Woody Fuel Loading
    WTOTLN = WTOTL * (1.0 - STL)						# Net Total Live Fuel Lodaing
    RHOBED = (WTOT - W1000) / fDEPTH					# Bulk density of the fuel bed
    RHOBAR = ((WTOTL * RHOL) + (WTOTD * RHOD)) / WTOT  # Weighted particle density of the fuel bed
    BETBAR = RHOBED / RHOBAR							# Ratio of bulk density to particle density

    # If live net fuel loading is greater than 0, calculate the 
           	# Live Fuel Moisture of Extinction
    if (WTOTLN > 0):
    
        HN1 = W1N * exp(-138.0 / SG1)
        HN10 =W10N  * exp(-138.0 / SG10)
        HN100 = W100N * exp(-138.0 / SG100)
        
        if ((-500 / SGHERB) < -180.218):
            HNHERB = 0
        else:
            HNHERB = WHERBN * exp(-500.0 / SGHERB)
        
        if ((-500 / SGWOOD) < -180.218):
            HNWOOD = 0
        else:
            HNWOOD = WWOODN * exp(-500.0 / SGWOOD)
        
        if ((HNHERB + HNWOOD) == 0):
            WRAT = 0
        else:
            WRAT = (HN1 + HN10 + HN100) / (HNHERB + HNWOOD)
        MCLFE = ((MC1 * HN1) + (MC10 * HN10) + (MC100 * HN100)) / (HN1 + HN10 + HN100)
        MXL = (2.9 * WRAT * (1.0 - MCLFE / MXD) - 0.226) * 100
        
    else:
        MXL = 0

    if (MXL < MXD):
        MXL = MXD
    SA1 = (W1P / RHOD) * SG1           # Surface area of dead 1hr fuel
    SA10 = (W10 / RHOD) * SG10         # Surface area of dead 10hr fuel
    SA100 = (W100 / RHOD) * SG100       # Surface area of dead 100hr fuel
    SAHERB = (WHERBP / RHOL) * SGHERB   # Surface area of live herbaceous fuel
    SAWOOD = (WWOOD / RHOL) * SGWOOD    # Surface area of live woody fuel
    SADEAD = SA1 + SA10 + SA100		# Surface area of dead fuel
    SALIVE = SAHERB + SAWOOD			# Surface area of live fuel

    
    if (SADEAD <= 0):
        return(0)

    F1 = SA1 / SADEAD      #Proportion of dead-fuel surface area in 1-hour class,used as a weighting factor for ROS calculation
    F10 = SA10 / SADEAD    #Proportion of dead-fuel surface area in 10-hour class,used as a weighting factor for ROS calculation
    F100 = SA100 / SADEAD  #Proportion of dead-fuel surface area in 100-hour class,used as a weighting factor for ROS calculation
    if (WTOTL <=0):
    
       FHERB = 0
       FWOOD = 0
    
    else:
    
        FHERB = SAHERB / SALIVE
        FWOOD = SAWOOD / SALIVE
    
    FDEAD = SADEAD / (SADEAD + SALIVE)		# Fraction of Dead Fuel Surface area to total loading
    FLIVE = SALIVE / (SADEAD + SALIVE)		# Fraction of Live Fuel Surface area to total loading
    WDEADN = (F1 * W1N) + (F10 * W10N) + (F100 * W100N)	# Weighted deaf-fuel loading

    if (SGWOOD > 1200 and SGHERB > 1200):
        WLIVEN = WTOTLN
    else:
        WLIVEN = (FWOOD * WWOODN) + (FHERB * WHERBN)

	# Characteristic surface area-to-volume ratio of dead fuel, surface area weighted
    SGBRD = (F1 * SG1) + (F10 * SG10) + (F100 * SG100)

	# Characteristic surface area-to-volume ratio of live fuel, surface area weighted.
    SGBRL = (FHERB * SGHERB) + (FWOOD * SGWOOD)

	# Characteristic surface area-to-volume ratio of fuel bed, surface area weighted.
    SGBRT = (FDEAD * SGBRD) + (FLIVE * SGBRL)

	# Optimum packing ratio, surface area weighted
    BETOP = 3.348 * pow(SGBRT, -0.8189)

	# Weighted maximum reaction velocity of surface area
    GMAMX = pow(SGBRT, 1.5) / (495.0 + 0.0594 * pow(SGBRT, 1.5))
    AD = 133 * pow(SGBRT, -0.7913)
	# Weighted optimum reaction velocity of surface area
    GMAOP = GMAMX * pow((BETBAR / BETOP), AD) * exp(AD * (1.0 - (BETBAR / BETOP)))

    ZETA = exp((0.792 + 0.681 * pow(SGBRT, 0.5)) * (BETBAR + 0.1))
    ZETA = ZETA / (192.0 + 0.2595 * SGBRT)

    WTMCD = (F1 * MC1) + (F10 * MC10) + (F100 * MC100)
    WTMCL = (FHERB * MCHERB) + (FWOOD * MCWOOD)
    DEDRT = WTMCD / MXD
    LIVRT = WTMCL / MXL
    ETAMD = 1.0 - 2.59 * DEDRT + 5.11 * pow(DEDRT,2.0) - 3.52 * pow(DEDRT, 3.0)
    ETAML = 1.0 - 2.59 * LIVRT + 5.11 * pow(LIVRT,2.0) - 3.52 * pow(LIVRT, 3.0)
    
    if (ETAMD < 0):
        ETAMD = 0
    if (ETAMD > 1):
        ETAMD = 1
    if (ETAML < 0):
        ETAML = 0
    if (ETAML > 1):
        ETAML = 1

    B = 0.02526 * pow(SGBRT, 0.54)
    C = 7.47 * exp(-0.133 * pow(SGBRT,0.55))
    E = 0.715 * exp(-3.59 * pow(10.0, -4.0) * SGBRT)
    
    UFACT = C * pow(BETBAR / BETOP, -1 * E)
    
    IR = GMAOP * ((WDEADN * HD * ETASD * ETAMD) + (WLIVEN * HD * ETASL * ETAML))
   
    fWNDFC = WNDFC

    if (88.0 * iWS * fWNDFC > 0.9 * IR):
        PHIWND = UFACT * pow(0.9 * IR, B)
    
    else:
        PHIWND = UFACT * pow(iWS * 88.0 * fWNDFC, B)
    

    # Actual slopes in degrees (>5) can now be input
    # Matches forumla used in WIMS developed by Larry Bradshaw (31 Aug 2016)
    slpfct = 0.267
    if iSlopeCls == 1:
      slpfct = 0.267
    elif iSlopeCls == 2:
        slpfct = 0.533
    elif iSlopeCls == 3:
        slpfct = 1.068
    elif iSlopeCls == 4:
        slpfct = 2.134
    elif iSlopeCls == 5:
        slpfct = 4.273
     
    

    PHISLP = slpfct * pow(BETBAR, -0.3)
    
    XF1 = F1 * exp(-138.0 /  (SG1)) * (250.0 + 11.16 * MC1)
    XF10 = F10 * exp(-138.0 / (SG10)) * (250.0 + 11.16 * MC10)
    XF100 = F100 * exp(-138.0 / (SG100)) * (250.0 + 11.16 * MC100)
    XFHERB = FHERB * exp(-138.0 /(SGHERB)) * (250.0 + 11.16 * MCHERB)
    XFWOOD = FWOOD * exp(-138.0 / (SGWOOD)) * (250.0 + 11.16 * MCWOOD)
    HTSINK = RHOBED * (FDEAD * (XF1 + XF10 + XF100) + FLIVE * (XFHERB + XFWOOD))
    
    fSC = IR * ZETA * (1.0 + PHISLP + PHIWND) / HTSINK
    
    F1E = W1P / WTOTD
    F10E = W10 / WTOTD
    F100E = W100 / WTOTD
    F1000E = W1000 / WTOTD
    
    if (WTOTL <=0):
        FHERBE = 0
        FWOODE = 0
    
    else:
        FHERBE = WHERBP / WTOTL
        FWOODE = WWOOD / WTOTL
    
    FDEADE = WTOTD / WTOT
    FLIVEE = WTOTL / WTOT
    WDEDNE = WTOTD * (1.0 - STD)
    WLIVNE = WTOTL * (1.0 - STL)
    SGBRDE = (F1E * SG1) + (F10E * SG10) + (F100E * SG100) + (F1000E * SG1000)
    
    SGBRLE = (FHERBE * SGHERB) + (FWOODE * SGWOOD)
    SGBRTE = (FDEADE * SGBRDE) + (FLIVEE * SGBRLE)
    BETOPE = 3.348 * pow(SGBRTE, -0.8189)
    GMAMXE = pow(SGBRTE, 1.5) / (495.0 + 0.0594 * pow(SGBRTE, 1.5))
    ADE = 133 * pow(SGBRTE, -0.7913)
    GMAOPE = GMAMXE * pow( (BETBAR/BETOPE), ADE) * exp(ADE * (1.0 - (BETBAR / BETOPE)))
    
    WTMCDE = (F1E * MC1) + (F10E * MC10) + (F100E * MC100) + (F1000E * MC1000)
    WTMCLE = (FHERBE * MCHERB) + (FWOODE * MCWOOD)
    DEDRTE = WTMCDE / MXD
    LIVRTE = WTMCLE / MXL
    ETAMDE = 1.0 - 2.0 * DEDRTE + 1.5 * pow(DEDRTE,2.0) - 0.5 * pow(DEDRTE, 3.0)
    ETAMLE = 1.0 - 2.0 * LIVRTE + 1.5 * pow(LIVRTE,2.0) - 0.5 * pow(LIVRTE, 3.0)
    if (ETAMDE < 0):
        ETAMDE = 0
    if (ETAMDE > 1):
        ETAMDE = 1
    if (ETAMLE < 0):
        ETAMLE = 0
    if (ETAMLE > 1):
        ETAMLE = 1

    IRE = (FDEADE * WDEDNE * HD * ETASD * ETAMDE)
    
    IRE = GMAOPE * (IRE + (FLIVEE * WLIVNE * (HD) * ETASL * ETAMLE))
    TAU = 384.0 / SGBRT
    fERC = 0.04 * IRE * TAU
    
    fBI = (.301 * pow((fSC * fERC), 0.46)) * 10.0
    ERC = fERC
    BI = fBI
    SC = fSC
    
    # Finally, calculate the Igntion Component
    TMPPRM = 0.0
    PNORM1 = 0.00232
    PNORM2 = 0.99767
    QIGN = 0.0
    CHI = 0.0
    PI = 0.0
    SCN = 0.0
    PFI = 0.0
    IC = 0.0
    if (SCM <= 0):
        IC = 0

    # Replace iTemp with the Nelson-derived fuel surface temperature
    TMPPRM = FuelTemperature

    QIGN = 144.5 - (0.266 * TMPPRM) - (0.00058 * TMPPRM * TMPPRM) - (0.01 * TMPPRM * MC1) + 18.54 * (1.0 - exp(-0.151 * MC1)) + 6.4 * MC1
    
    if (QIGN >= 344.0):
        IC = 0

    CHI = (344.0 - QIGN) / 10.0
    if ((pow(CHI, 3.66) * 0.000923 / 50) <= PNORM1):
        IC = 0

    PI = ((pow(CHI, 3.66) * 0.000923 / 50) - PNORM1) * 100.0 / PNORM2
    if (PI < 0):
        PI = 0
    if (PI > 100):
        PI = 100
    SCN = 100.0 * SC / SCM
    if (SCN > 100.0):
        SCN = 100.0
    PFI = pow(SCN, 0.5)
    IC = 0.10 * PI * PFI
    
    if (SC < 0.00001):
        IC = 0

       
    return ([round(ERC,2),round(SC,2),round(BI,2),round(IC,2)])
