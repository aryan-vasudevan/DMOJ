#include <iostream>

int main() {
    int antennae, eyes;
    std::cin >> antennae;
    std::cin >> eyes;

    if (antennae >= 3 && eyes <= 4) {
        std::cout << "TroyMartian\n";
    }
    if (antennae <= 6 && eyes >= 2) {
        std::cout << "VladSaturnian\n";
    }
    if (antennae <= 2 && eyes <= 3) {
        std::cout << "GraemeMercurian\n";
    }

    return 0;
}