from django.urls import path
from . import views


urlpatterns = [
    path('', views.CSS_home, name="CSS_home"),
    path('selectors/', views.CSS_selectors, name="CSS_selectors"),
    path('box-model/', views.CSS_box_model, name="CSS_box_model"),
    path(
        'display-and-positioning/',
        views.CSS_display_and_positioning,
        name="CSS_display_and_positioning"
    ),
    path('flexbox/', views.CSS_flexbox, name="CSS_flexbox"),
    path('grids/', views.CSS_grids, name="CSS_grids"),
    path('backgrounds/', views.CSS_backgrounds, name="CSS_backgrounds"),
]
