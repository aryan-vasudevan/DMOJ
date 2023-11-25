#include <iostream>

int main() {
    int limit, speed;
    std::cin >> limit;
    std::cin >> speed;

    int d = speed - limit;

    if (d > 30) {
        std::cout << "You are speeding and your fine is $500.";
    } else if (d > 21) {
        std::cout << "You are speeding and your fine is $270.";
    } else if (d > 1) {
        std::cout << "You are speeding and your fine is $100.";
    } else {
        std::cout << "Congratulations, you are within the speed limit!";
    }

    return 0;
}