#include <iostream>
#include <map>
#include <string>

int main() {
    std::map<std::string, int> peppers = {
        {"Poblano", 1500},
        {"Mirasol", 6000},
        {"Serrano", 15500},
        {"Cayenne", 40000},
        {"Thai", 75000},
        {"Habanero", 125000}
    };

    int N;
    std::cin >> N;

    int res = 0;
    for (int i = 0; i < N; ++i) {
        std::string pepper;
        std::cin >> pepper;
        res += peppers[pepper];
    }

    std::cout << res;

    return 0;
}