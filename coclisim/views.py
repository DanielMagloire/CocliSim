from rest_framework.response import Response
from rest_framework import generics
from . models import *

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

class PlotConfortView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):

        CLO = float(request.GET.get('CLO'))
        MET = float(request.GET.get('MET'))
        WME = float(request.GET.get('WME'))
        TA = float(request.GET.get('TA'))
        TR = float(request.GET.get('TR'))
        VEL = float(request.GET.get('VEL'))
        RH = float(request.GET.get('RH'))
        PA = float(request.GET.get('PA'))

        calcul = PlotConfortClass(CLO, MET, WME, TA, TR, RH, VEL, PA)
        result = calcul.initPlotConfort()

        return Response(result)

class PointPpdView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):

        CLO = float(request.GET.get('CLO'))
        MET = float(request.GET.get('MET'))
        WME = float(request.GET.get('WME'))
        TA = float(request.GET.get('TA'))
        TR = float(request.GET.get('TR'))
        VEL = float(request.GET.get('VEL'))
        RH = float(request.GET.get('RH'))
        PA = float(request.GET.get('PA'))

        calcul = PlotConfortClass(CLO, MET, WME, TA, TR, RH, VEL, PA)
        result = calcul.CalculConfortClimatique()

        return Response(result)

class PlotAshraeView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):

        CLO = float(request.GET.get('CLO'))
        MET = float(request.GET.get('MET'))
        WME = float(request.GET.get('WME'))
        TA = float(request.GET.get('TA'))
        TR = float(request.GET.get('TR'))
        VEL = float(request.GET.get('VEL'))
        RH = float(request.GET.get('RH'))
        PA = float(request.GET.get('PA'))

        calcul = PlotAshraeClass(CLO, MET, WME, TA, TR, RH, VEL, PA)
        result = calcul.initPlotAshrae()

        return Response(result)

class PointAshraeView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):

        CLO = float(request.GET.get('CLO'))
        MET = float(request.GET.get('MET'))
        WME = float(request.GET.get('WME'))
        TA = float(request.GET.get('TA'))
        TR = float(request.GET.get('TR'))
        VEL = float(request.GET.get('VEL'))
        RH = float(request.GET.get('RH'))
        PA = float(request.GET.get('PA'))

        calcul = PlotAshraeClass(CLO, MET, WME, TA, TR, RH, VEL, PA)
        result = calcul.CalculHumiSpeci()
        return Response(result)

class PlotTurbulenceView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):

        tAir2 = float(request.GET.get('tAir2'))
        vAir2 = float(request.GET.get('vAir2'))
        turbulence = float(request.GET.get('turbulence'))
        
        calcul = PlotTurbulenceClass(tAir2, vAir2, turbulence)
        result = calcul.initPlotTurbulence()

        return Response(result)

class PointTurbulenceView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):

        tAir2 = float(request.GET.get('tAir2'))
        vAir2 = float(request.GET.get('vAir2'))
        turbulence = float(request.GET.get('turbulence'))
        
        calcul = PlotTurbulenceClass(tAir2, vAir2, turbulence)

        calcul = PlotTurbulenceClass(tAir2, vAir2, turbulence)
        result = calcul.updatePlotTurbulence()
        return Response(result)

class PlotAsymTView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):

        deltaTv = float(request.GET.get('deltaTv'))
        tSol = float(request.GET.get('tSol'))
        tAsym = float(request.GET.get('tAsym'))
        typeParoi = float(request.GET.get('typeParoi'))
        
        calcul = PlotDeltaTvClass(deltaTv, tSol, tAsym, typeParoi)
        result = calcul.initPlotAsymT()

        return Response(result)

class PointAsymTView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):

        deltaTv = float(request.GET.get('deltaTv'))
        tSol = float(request.GET.get('tSol'))
        tAsym = float(request.GET.get('tAsym'))
        typeParoi = float(request.GET.get('typeParoi'))

        calcul = PlotDeltaTvClass(deltaTv, tSol, tAsym, typeParoi)
        result = calcul.updatePlotAsymT()
        return Response(result)

class PlotTsolView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):

        deltaTv = float(request.GET.get('deltaTv'))
        tSol = float(request.GET.get('tSol'))
        tAsym = float(request.GET.get('tAsym'))
        typeParoi = float(request.GET.get('typeParoi'))
        
        calcul = PlotDeltaTvClass(deltaTv, tSol, tAsym, typeParoi)
        result = calcul.initPlotTsol()

        return Response(result)

class PointTsolView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):

        deltaTv = float(request.GET.get('deltaTv'))
        tSol = float(request.GET.get('tSol'))
        tAsym = float(request.GET.get('tAsym'))
        typeParoi = float(request.GET.get('typeParoi'))

        calcul = PlotDeltaTvClass(deltaTv, tSol, tAsym, typeParoi)
        result = calcul.updatePlotTsol()
        return Response(result)

class PlotDeltaTvView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):

        deltaTv = float(request.GET.get('deltaTv'))
        tSol = float(request.GET.get('tSol'))
        tAsym = float(request.GET.get('tAsym'))
        typeParoi = float(request.GET.get('typeParoi'))
        
        calcul = PlotDeltaTvClass(deltaTv, tSol, tAsym, typeParoi)
        result = calcul.initPlotDeltaTv()

        return Response(result)

class PointDeltaTvView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):

        deltaTv = float(request.GET.get('deltaTv'))
        tSol = float(request.GET.get('tSol'))
        tAsym = float(request.GET.get('tAsym'))
        typeParoi = float(request.GET.get('typeParoi'))

        calcul = PlotDeltaTvClass(deltaTv, tSol, tAsym, typeParoi)
        result = calcul.updatePlotDeltaTv()
        return Response(result)

