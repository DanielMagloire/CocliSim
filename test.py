#!/usr/bin/env python3

import math

def fnps(T):
        valFnps = math.exp(16.6536 - 4030.183 / (T + 235))
        return valFnps

def CalculConfortClimatique(TA, TR, RH, VEL, CLO, MET, PA, WME):
    if PA == 0:
        PA = RH * 10 * fnps(TA)
    ICL = 0.155 * CLO
    M  = MET * 58.15
    W  = WME * 58.15
    MW  = M - W
    FCL  = 0
    if ICL < 0.078:
        FCL = 1 + 1.29 * ICL
    else:
        FCL = 1.05 + 0.645 * ICL
    HCF  = 12.1 * math.sqrt(VEL)
    TAA  = TA + 273
    TRA  = TR + 273
    
    TCLA  = TAA + (35.5 - TA) / (3.5 * (6.45 * ICL + 0.1))
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
    HL4  = 0.0014 * M * (34 - TA)
    HL5  = 3.96 * FCL * (math.pow(XN, 4) - math.pow(TRA / 100, 4))
    HL6  = FCL * HC * (TCL - TA)
    TS  = 0.303 * math.exp(-0.036 * M) + 0.028
    PMV = TS * (MW - HL1 - HL2 - HL3 - HL4 - HL5 - HL6)
    if (PMV < -3):
        PMV = -3
    if (PMV > 3):
        PMV = 3
    PPD = 100 - 95 * math.exp(-0.03353 * math.pow(PMV, 4) - 0.2179 * math.pow(PMV, 2))
    return([PMV, PPD])
    
test = CalculConfortClimatique(20, 22, 50, 0.1, 1, 1.3, 0, 0)
print(test)

        initPlotAshrae: function () {
            var x = []
            var y = []
            var line = []
            var area = []
            var plot = []
            var temp = []
            for(var i=0;i<5;i++){
                x = []
                y = []
                area = []
                temp.push(this.APICourbeAshrea[i])
                if(i==0||i==3) {
                    for(var j=0;j<5;j++){
                        x.push(temp[j][0])
                        y.push(temp[j][1])
                    }
                    for (j=0; j<5; j++) {
                        area.push([x[j], y[j]])
                    }
                }
                if(i==1||i==2||i==4) {
                    for(j=0;j<4;j++){
                        x.push(temp[j][0])
                        y.push(temp[j][1])
                    }
                    for (j=0; j<5; j++) {
                        area.push([x[j], y[j]])
                    }
                }
                plot.push(area)
                temp = []
            }
            for (i=5;i<10;i++){
                x = []
                y = []
                line = []
                for (j=0; j<21; j++) {
                    x.push(this.APICourbeAshrea[i][j][0])
                    y.push(this.APICourbeAshrea[i][j][1])
                }
                for (j=0; j<21; j++) {
                    line.push([x[j], y[j]])
                }
                plot.push(line)
            }
            return plot
        },