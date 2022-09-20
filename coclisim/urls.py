from django.contrib import admin
from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^plotconfort/$', PlotConfortView.as_view(), name='plot_confort_view'),
    re_path(r'^pointppd/$', PointPpdView.as_view(), name='point_ppd_view'),

    re_path(r'^plotashrae/$', PlotAshraeView.as_view(), name='plot_ashrae_view'),
    re_path(r'^pointashrae/$', PointAshraeView.as_view(), name='point_ashrae_view'),
    
    re_path(r'^plotturbulence/$', PlotTurbulenceView.as_view(), name='plot_turbulence_view'),
    re_path(r'^pointturbulence/$', PointTurbulenceView.as_view(), name='point_turbulence_view'),
    
    re_path(r'^plotdeltatv/$', PlotDeltaTvView.as_view(), name='plot_deltatv_view'),
    re_path(r'^pointdeltatv/$', PointDeltaTvView.as_view(), name='point_deltatv_view'),
    
    re_path(r'^plotasymt/$', PlotAsymTView.as_view(), name='point_asymt_view'),
    re_path(r'^pointasymt/$', PointAsymTView.as_view(), name='point_asymt_view'),
    
    re_path(r'^plottsol/$', PlotTsolView.as_view(), name='plot_tsol_view'),
    re_path(r'^pointtsol/$', PointTsolView.as_view(), name='point_tsol_view'),
]
