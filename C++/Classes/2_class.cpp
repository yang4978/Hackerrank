//https://www.hackerrank.com/challenges/c-tutorial-class/problem

#include <iostream>
#include <sstream>
using namespace std;

class Student{
    private:
        int age;
        string first_name;
        string last_name;
        int standard;
    public:
        void set_age(int val){
            age = val;
        }
        int get_age(){
            return age;
        }

        void set_first_name(string val){
            first_name = val;
        }
        string get_first_name(){
            return first_name;
        }

        void set_last_name(string val){ 
            last_name = val; 
        }
        string get_last_name(){
            return last_name; 
        }

        void set_standard(int val){
            standard = val; 
        }
        int get_standard(){
            return standard; 
        }

        string to_string(){
            stringstream result;
            char c = ',';
            result<<age<<c<<first_name<<c<<last_name<<c<<standard;           
            return result.str();
        }
};

int main() {
    int age, standard;
    string first_name, last_name;
    
    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();
    
    return 0;
}
