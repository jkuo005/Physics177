//=Lab1 ex3a=
//This is written to calculate the time it would take
//for an object with an initial velocity go from a variable
//height to a lower height.
//    written by Jeff Kuo, 860884131

#include <iostream>
#include <cmath>

using namespace std;

int main() 
{
    double variX = 0.0; //Change in Distance
    double variH = 0.0; //initial Height
    double variS = 0.0; //Final Height
    double variT = 0.0; //time elapsed
    double variVi= 0.0; //initial velocity
    double variVf= 0.0; //final velocity   
    double consG = 9.81;//gravity
    double varidV= 0.0; //change in velocity
    
//Data Inquiry

    cout << "Hello, please keep all units in meters and seconds!" << endl;
    cout << "Also, the direction of gravity is positive (downwards)."<< endl;
    cout << "If an initial velocity is thrown upwards, " << endl;
    cout << "please kindly put a negative sign in front of the initial velocity value." << endl << endl;
    cout << "Enter initial velocity: ";
    cin  >> variVi;
    cout << variVi << " meters per second" << endl;
    cout << "Enter initial height: ";
    cin  >> variH;
    cout << variH << " meters" << endl;
    cout << "Enter final height: ";
    cin  >> variS;
    cout << variS << " meters" << endl;

//Calculation

    variX = variH - variS;
    cout << "The change in distance is " << variX  << " meters"              << endl;
    
    variVf = sqrt( pow(variVi,2) + ( 2 * consG * variX) );
    cout << "The final velocity is "     << variVf << " meters per second"   << endl;
    
    varidV = variVf - variVi;
    cout << "The change in velocity is " << varidV << " meters per second"   << endl;
        
    variT = ( (variVf - variVi) / consG );
    cout << "Total time elapsed is "     << variT  << " seconds"             << endl;
    
    return 0;
}