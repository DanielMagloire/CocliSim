from django.db import models
import math

class PlotConfortClass(object):

    def __init__(self, CLO, MET, WME, TA, TR, RH, VEL, PA): 
        self.TA = TA
        self.TR = TR
        self.RH = RH
        self.VEL = VEL
        self.CLO = CLO
        self.MET = MET
        self.PA = PA
        self.WME = WME
        pass

    def fnps(self):
        valFnps = math.exp(16.6536 - 4030.183 / (self.TA + 235))
        return valFnps

    def initPlotConfort(self):
        courbePpd = []
        for i in range(-30, 31):
            courbePpd.append([i/10, self.ppd(i/10)])
        return courbePpd

    def CalculConfortClimatique(self):
        if self.PA == 0:
            PA = self.RH * 10 * self.fnps()
        ICL = 0.155 * self.CLO
        M  = self.MET * 58.15
        W  = self.WME * 58.15
        MW  = M - W
        FCL  = 0
        if ICL < 0.078:
            FCL = 1 + 1.29 * ICL
        else:
            FCL = 1.05 + 0.645 * ICL
        HCF  = 12.1 * math.sqrt(self.VEL)
        TAA  = self.TA + 273
        TRA  = self.TR + 273
        
        TCLA  = TAA + (35.5 - self.TA) / (3.5 * (6.45 * ICL + 0.1))
        P1  = ICL * FCL
        P2  = P1 * 3.96
        P3  = P1 * 100
        P4  = P1 * TAA
        P5  = 308.7 - 0.028 * MW + P2 * math.pow(TRA / 100, 4)
        XN  = TCLA / 100
        XF  = XN
        N = 0
        HC = 0
        HCN  = 0
        EPS  = 0.00015
        DO = True
        while DO:
            XF = (XF + XN) / 2
            HCN = 2.38 * math.pow(abs(100 * XF - TAA), 0.25)
            if (HCF > HCN):
                HC = HCF
            else:
                HC = HCN
            XN = (P5 + P4 * HC - P2 * math.pow(XF, 4)) / (100 + P3 * HC)
            N = N + 1
            if (N > 150):
                PMV = 999999
                PPD = 100
                return
            if (abs(XN - XF) <= EPS):
                DO = False
        TCL  = 100 * XN - 273
        HL1  = 3.05 * 0.001 * (5733 - 6.99 * MW - PA)
        HL2  = 0
        if (MW > 58.15):
            HL2 = 0.42 * (MW - 58.15)
        else:
            HL2 = 0
        HL3  = 1.7 * 0.00001 * M * (5867 - PA)
        HL4  = 0.0014 * M * (34 - self.TA)
        HL5  = 3.96 * FCL * (math.pow(XN, 4) - math.pow(TRA / 100, 4))
        HL6  = FCL * HC * (TCL - self.TA)
        TS  = 0.303 * math.exp(-0.036 * M) + 0.028
        PMV = TS * (MW - HL1 - HL2 - HL3 - HL4 - HL5 - HL6)
        if (PMV < -3):
            PMV = -3
        if (PMV > 3):
            PMV = 3
        PPD = 100 - 95 * math.exp(-0.03353 * math.pow(PMV, 4) - 0.2179 * math.pow(PMV, 2))
        return ([PMV, PPD])

    def ppd(self, pmv):
        valPpd = 100 - 95 * math.exp(-0.03353 * math.pow(pmv, 4) - 0.2179 * math.pow(pmv, 2))
        return valPpd


class PlotAshraeClass(object):
    def __init__(self, CLO, MET, WME, TA, TR, RH, VEL, PA): 
        self.TA = TA
        self.TR = TR
        self.RH = RH
        self.VEL = VEL
        self.CLO = CLO
        self.MET = MET
        self.PA = PA
        self.WME = WME
        pass

    def PvapSat(self, tAir):
        if (tAir < 0):
            valPvapSat = math.pow(10, (2.78771 + (9.756 * tAir) / (272.7 + tAir)))
        else:
            valPvapSat = math.pow(10, (2.78771 + (7.625 * tAir) / (241 + tAir)))

        return valPvapSat
    

    def SpeciHumi(self, tAir, hRel, pAtmos):
        pAtmos = 101325
        pVap = 0.01 * hRel * self.PvapSat(tAir)
        valSpeciHumi = 0.622 * pVap / (pAtmos - pVap)
        return valSpeciHumi
    
    def initPlotAshrae(self):
        valHumiAbaques = [30, 50, 60, 70, 100]
        plotDataAshrae = []
        zoneHiver1 = [[20, 4.5], [20, 1000 * self.SpeciHumi(20, 60, 101325)], [23.5, 1000 * self.SpeciHumi(23.5, 60, 101325)], [23.5, 4.5]]
        zoneHiver2 = [[23.5, 4.5], [23.5, 1000 * self.SpeciHumi(23.5, 60, 101325)], [24.5, 4.5]]
        zoneEte1 = [[22.5, 1000 * self.SpeciHumi(22.5, 60, 101325)],  [23.2, 1000 * self.SpeciHumi(23.2, 60, 101325)], [23.2, 4.5]]
        zoneEte2 = [[23.2, 4.5], [23.2, 1000 * self.SpeciHumi(23.2, 60, 101325)], [25.5, 1000 * self.SpeciHumi(25.5, 60, 101325)], [25.5, 4.5]]
        zoneEte3 = [[25.5, 4.5], [25.5, 1000 * self.SpeciHumi(25.5, 60, 101325)], [27, 4.5]]
        plotDataAshrae.append(zoneHiver1)
        plotDataAshrae.append(zoneHiver2)
        plotDataAshrae.append(zoneEte1)
        plotDataAshrae.append(zoneEte2)
        plotDataAshrae.append(zoneEte3)
        for j in range(0,5):
            courbeHumiSpeci = []
            for i in range(15,36):
                courbeHumiSpeci.append([ i, 1000 * self.SpeciHumi(i, valHumiAbaques[j], 101325) ])
            plotDataAshrae.append(courbeHumiSpeci)
        return plotDataAshrae

    def tOperative(self, tAir, tRay, vAir):
        a = 0.5 + 0.25 * vAir
        valToperative = a * tAir + (1 - a) * tRay
        return valToperative

    def CalculHumiSpeci(self):
        pointHumiSpeci = []
        tOp = self.tOperative(self.TA, self.TR, self.VEL)
        humiSpeci = 1000 * self.SpeciHumi(self.TA, self.RH, 101325)
        pointHumiSpeci = [tOp, humiSpeci]
        return pointHumiSpeci

class PlotTurbulenceClass(object):
    
    def __init__(self, tAir2, vAir2, turbulence):
        self.tAir2 = tAir2
        self.vAir2 = vAir2
        self.turbulence = turbulence
        pass

    def draughtRate(self, tAir, vAir, turbulence):
        if(vAir<0.05):
            vAir = 0.05
        valDraughtRate = (34 - tAir) * (0.37 * vAir * turbulence + 3.14) * math.pow(vAir - 0.05, 0.62)
        if ( valDraughtRate > 100 ):
            valDraughtRate = 100
        if ( valDraughtRate < 1 ):
            valDraughtRate = 1
        return valDraughtRate

    def initPlotTurbulence(self):
        tAir2 = self.tAir2
        turbulence = self.turbulence
        courbePpdTurbulence = []
        for i in range(5,51):
            courbePpdTurbulence.append([i/100, self.draughtRate(tAir2, i/100, turbulence)])
        return courbePpdTurbulence

    def updatePlotTurbulence(self):
        tAir2 = self.tAir2
        vAir2 = self.vAir2
        turbulence = self.turbulence
        pointPpdTurbulence = []
        pointPpdTurbulence.append([vAir2, self.draughtRate(tAir2, vAir2, turbulence)])
        return pointPpdTurbulence

class PlotDeltaTvClass(object):
    
    def __init__(self, deltaTv, tSol, tAsym, typeParoi):
        self.deltaTv = deltaTv
        self.tSol = tSol
        self.tAsym = tAsym
        self.typeParoi = typeParoi
        pass

    def ppdDeltaTv(self, DeltaTv):
        valPpdDeltaTv = 100 / (1 + math.exp(5.76 - 0.856 * DeltaTv))
        return valPpdDeltaTv


    def ppdTsol(self, tSol):
        valPpdTsol = 100 - 94 * math.exp(-1.387 + 0.118 * tSol - 0.0025 * math.pow(tSol, 2))
        return valPpdTsol

    def ppdAsymT(self, typeParoi, Tasym):
        valPpdAsymT = 0
        if(typeParoi == 0):
            valPpdAsymT = 100 / (1 + math.exp(2.84 - 0.174 * Tasym)) - 5.5
        if(typeParoi == 1):
            valPpdAsymT = -1.2568 + 0.0189 * math.exp(1.9469 * math.pow(Tasym, 0.47))
        if(typeParoi == 2):
            valPpdAsymT = -0.1056 + 0.0163 * math.exp(1.5847 * math.pow(Tasym, 0.49))
        if(typeParoi == 3):
            valPpdAsymT = -0.1112 + 0.0539 * math.exp(1.4686 * math.pow(Tasym, 0.36))
        return valPpdAsymT

    def initPlotDeltaTv(self):
        courbePpdDeltaTv = []
        for i in range(0,41):
            courbePpdDeltaTv.append([i/5, self.ppdDeltaTv(i/5)])
        return courbePpdDeltaTv

    def initPlotTsol(self):
        courbePpdTsol = []
        for i in range (25,226):
            courbePpdTsol.append([i/5, self.ppdTsol(i/5)])
        return courbePpdTsol

    def initPlotAsymT(self):
        courbeAsymT = []
        plotDataAsymT = []
        for i in range (1,24):
            courbeAsymT.append([i, self.ppdAsymT(0, i)])
        plotDataAsymT.append(courbeAsymT)
        courbeAsymT = []
        for i in range(6,18):
            courbeAsymT.append([i, self.ppdAsymT(1, i)])
        plotDataAsymT.append(courbeAsymT)
        courbeAsymT = []
        for i in range (7,18):
            courbeAsymT.append([i, self.ppdAsymT(2, i)])
        plotDataAsymT.append(courbeAsymT)
        courbeAsymT = []
        for i in range(7,32):
            courbeAsymT.append([i, self.ppdAsymT(3, i)])
        plotDataAsymT.append(courbeAsymT)
        return plotDataAsymT
    
    def updatePlotDeltaTv(self):
        deltaTv = self.deltaTv
        pointPpdDeltaTv = []
        pointPpdDeltaTv.append([deltaTv, self.ppdDeltaTv(deltaTv)])
        return pointPpdDeltaTv

    def updatePlotTsol(self):
        tSol = self.tSol
        pointPpdTsol = []
        pointPpdTsol.append([tSol, self.ppdTsol(tSol)])
        return pointPpdTsol
    
    def updatePlotAsymT(self):
        tAsym = self.tAsym
        typeParoi = self.typeParoi
        pointPpdAsymT = [tAsym, self.ppdAsymT(typeParoi, tAsym)]
        return pointPpdAsymT
