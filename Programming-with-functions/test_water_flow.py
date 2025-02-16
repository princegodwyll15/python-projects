from pytest import approx
import pytest
from water_flow import pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction,water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, convert_kpa_to_psi

#testing water column height
def test_water_column_height():
    #test in a case where tower height =0.0 and tank wall height= 0.0
    assert water_column_height(t=0.0, w=0.0) == 0.0
    #test in a case where tower height =0.0 and tank wall height= 0.0
    assert water_column_height(t=0.0, w=10.0) == 7.5
    #test in a case where tower height =0.0 and tank wall height= 0.0
    assert water_column_height(t=25.0, w=0.0) == 25.0
    #test in a case where tower height =0.0 and tank wall height= 0.0
    assert water_column_height(t=48.3, w=12.8) == 57.9



#testing the pressure gain from water height
def test_pressure_gain_from_water_height():
    #test in a case where where height = 0.0 and tolerance is 0.001
    assert pressure_gain_from_water_height(height=0.0) == approx(0.000, abs=0.001)
    #test in a case where where height = 0.0 and tolerance is 0.001
    assert pressure_gain_from_water_height(height=30.2) == approx(295.628, abs=0.001)
    #test in a case where where height = 0.0 and tolerance is 0.001
    assert pressure_gain_from_water_height(height=50.0) == approx(489.450, abs=0.001)



#testing pressure lost from pipe
def test_pressure_lost_from_pipe ():
    # def pressure_lost_from_pipe(d, L, f, v):
    # d is the diameter of the pipe in meters
    # L is the length of the pipe in meters
    # f is the pipe's friction factor
    # v velocity of the water flowing through the pipe in meters/second(fluid_velocity)
    # p is the density of water  998.2 (kilogram / meter^3)
    assert pressure_loss_from_pipe(d=0.048692, L=0.00, f=0.018, v=1.75) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(d=0.048692, L=200.00, f=0.000, v=1.75) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(d=0.048692, L=200.00, f=0.018, v=0.00) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(d=0.048692, L=200.00, f=0.018, v=1.75) == approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe(d=0.048692, L=200.00, f=0.018, v=1.65) == approx(-100.462, abs=0.001)
    assert pressure_loss_from_pipe(d=0.286870, L=1000.00, f=0.013, v=1.65) == approx(-61.576, abs=0.001)
    assert pressure_loss_from_pipe(d=0.286870, L=1800.75, f=0.013, v=1.65) == approx(-110.884, abs=0.001)

def text_reynolds_number ():
    assert reynolds_number(d=0.048692, v=0.00) == approx(0, abs=1)
    assert reynolds_number(d=0.048692, v=1.65) == approx(80069, abs=1)
    assert reynolds_number(d=0.048692, v=1.75) == approx(84922, abs=1)
    assert reynolds_number(d=0.286870, v=1.65) == approx(471729,abs=1)
    assert reynolds_number(d=0.286870, v=1.75) == approx(500318,abs=1)

def test_pressure_loss_from_fittings ():
    assert pressure_loss_from_fittings(v=0.00, n=3) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(v=1.65, n=0) == approx(0.000, abs=0.001)    
    assert pressure_loss_from_fittings(v=1.65, n=2) == approx(-0.109, abs=0.001)
    assert pressure_loss_from_fittings(v=1.75, n=2) == approx(-0.122, abs=0.001)
    assert pressure_loss_from_fittings(v=1.75, n=5) == approx(-0.306, abs=0.001)

def test_pressure_loss_from_pipe_reduction ():
    assert pressure_loss_from_pipe_reduction (D=0.28687, v=0.00, R=1, d=0.048692) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe_reduction (D=1.65, v=0.00, R=471729, d=0.048692) == approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction (D=1.65, v=0.00, R=500318, d=0.048692) == approx(-184.182, abs=0.001)


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
