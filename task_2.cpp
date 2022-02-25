#include <iostream>
#include <string>
using namespace std;


class EMPLOYEE {
    
	string organization;
	string position;
	double experience;
	string name;
	char gender;
	int age;
	double salary;
	
public:

	static int count;
	EMPLOYEE (string organization, string position, double experience, string name, char gender, int age, double salary)
	{
		this -> organization = organization;
		this -> position = position;
		this -> experience = experience;
		this -> name = name;
		this -> gender = gender;
		this -> age = age;
		this -> salary = salary;
		count += 1;
	}
	void GetWorkInfo() {
		cout << "Organization: " << organization << endl;
		cout << "Position: " << position << endl;
		cout << "Experience: " << experience << endl;
		cout << "Salary: " << salary << endl;
	}
	void SetPosition(string position) {
		this -> position = position;
	}
	void SetSalary(double valueSalary) {
		salary = valueSalary + salary;
	}
	void GetPersonalInfo() {
		cout << "Name: " << name << endl;
		cout << "Gender: " << gender << endl;
		cout << "Age: " << age << endl;
	}
	static void showCount()
	{
		cout << "Number_of_employees: " << count << endl;
	}
	void SalaryComparsion(EMPLOYEE& second) {
		if (*this < second) {
			cout << second.name << " has a salary greater than " << this -> name << endl;	// операция сравнения
		}
		else if (*this == second) {
			cout << second.name << " has the same salary than " << this -> name << endl;
		}
		else cout << this->name << " has a salary less than " << second.name << endl;
	}
	bool operator < (EMPLOYEE const& other) {
		return this->salary < other.salary;
	}											// перегрузка операций
	bool operator == (EMPLOYEE const& other) {
		return this->salary == other.salary;
	}
	void SalaryAssignment(EMPLOYEE& second) {
		this->salary = second.salary;		// операция присваивания
	}
	~EMPLOYEE() {
		count -= 1;
	}
};
int EMPLOYEE::count = 0;


int main() {
    
	setlocale(LC_ALL, "Russian");
	EMPLOYEE emp1("Yandex", "Junior_developer", 1, "Shamko Maxim Leonidovich", 'М', 18, 40000);
	EMPLOYEE emp2("Yandex", "Senior", 7, "Kirsanov Pavel Antonovich", 'М', 28, 200000);
	EMPLOYEE employees[2] = {emp1, emp2};
	EMPLOYEE::showCount();
	for (int i = 0; i < 2; i++)
	{
		employees[i].GetPersonalInfo();
		employees[i].GetWorkInfo();
		cout << endl;
	}
	employees[0].SalaryComparsion(employees[1]);
	employees[0].SetPosition("Middle"); // изменяем должность первого сотрудника
	employees[0].SetSalary(10000); // поднимаем зарплату первого сотрудника
	employees[0].SalaryAssignment(employees[1]); // устанавливаем первому сотруднику зарплату второго
	for (int i = 0; i < 2; i++)
	{
		employees[i].GetPersonalInfo();
		employees[i].GetWorkInfo();
		cout << endl;
	}
}