#include <iostream>
#include <string>

double planA(int dayTime, int eveTime, int weekendTime);
double planB(int dayTime, int eveTime, int weekendTime);


int main() {
    int dayTime, eveTime, weekendTime;
    std::cin >> dayTime;
    std::cin >> eveTime;
    std::cin >> weekendTime;

    double planAPrice = planA(dayTime, eveTime, weekendTime);
    double planBPrice = planB(dayTime, eveTime, weekendTime);
    std::string compareDouble(double a, double b);

    std::cout << "Plan A costs " << planAPrice << "\n";
    std::cout << "Plan B costs " << planBPrice << "\n";

    if (compareDouble(planAPrice, planBPrice) == "greater") {
        std::cout << "Plan B is cheapest.";
    } else if (compareDouble(planAPrice, planBPrice) == "lesser") {
        std::cout << "Plan A is cheapest.";
    } else {
        std::cout << "Plan A and B are the same price.";
    }

    return 0;
}

double planA(int dayTime, int eveTime, int weekendTime) {
    double dayPrice = 0;

    if (dayTime > 100) {
        dayPrice = (dayTime - 100) * 0.25;
    }
    
    double evePrice = eveTime * 0.15;
    double weekendPrice = weekendTime * 0.20;
    
    return dayPrice + evePrice + weekendPrice;
}

double planB(int dayTime, int eveTime, int weekendTime) {
    double dayPrice = 0;

    if (dayTime > 250) {
        dayPrice = (dayTime - 250) * 0.45;
    }

    double evePrice = eveTime * 0.35;
    double weekendPrice = weekendTime * 0.25;

    return dayPrice + evePrice + weekendPrice;
}

std::string compareDouble(double a, double b) {
    if (abs(a - b) < 0.01) {
        return "equal";
    } else if ((a - b) > 0) {
        return "greater";
    } else {
        return "lesser";
    }
}