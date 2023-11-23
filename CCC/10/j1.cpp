#include <iostream>
#include <cmath>

int main() {
    int target, leftHand, res;
    std::cin >> target;

    if (target > 5) {
        leftHand = 5;
    } else {
        leftHand = target;
    }

    res = 0;

    while (leftHand >= ceil((double) target / 2) ) {
        res += 1;
        leftHand -= 1;
    }

    std::cout << res;

    return 0;
}