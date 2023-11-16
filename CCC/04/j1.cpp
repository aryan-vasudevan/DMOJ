#include <iostream>
#include <cmath>

int main() {
    int tiles;
    std::cin >> tiles;

    int ans = (int) std::sqrt(tiles);

    std::cout << "The largest square has side length " << ans << ".";

    return 0;
}