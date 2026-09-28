#include <iostream>
#include <string>
#include <memory> // wymagane do smart pointers

// klasa rprezentujaca uzytkownika homelabu
class uzytkownik {
    private:
        std::string imie;
        std::string rola;
    
    public:
        uzytkownik(std::string i, std::string r) : imie(i), rola(r) {}

        void przywitaj() {
            std::cout << "Witaj" << imie << "! Twoja rola na serwerze to: " << rola << ".\n";
        }
};

int main(){
    std::cout << "--- C++ Smart Pointers ---\n";

    // zamiast 'new uzytkownik(...)', uzywamy dla bezpieczenstwa std::make_unique
    std::unique_ptr<uzytkownik> admin = std::make_unique<uzytkownik>("Janek", "Administrator DevLab");

    //wywolanie smart pointers
    admin->przywitaj();

    std::cout << "Program work end, memory after object are free!\n";
    return 0;
}