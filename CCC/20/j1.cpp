#include <iostream>

int main() {
    int s, m, l;
    std::cin >> s >> m >> l;

    if (s + 2 * m + 3 * l >= 10) {
        std::cout << "happy";
    } else {
        std::cout << "sad";
    }

    return 0;
}