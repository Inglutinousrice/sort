
#include<iostream>

using namespace std;

// 삽입 정렬 함수 선언
void insertionSort(int arr[], int size);

// 메인 함수
int main() {
	int myArr[7] = { 7, 2, 5, 1, 9, 11, 4 };
	insertionSort(myArr, 7);
	for (int i = 0; i < 7; ++i)
		cout << myArr[i] << "  ";
	return 0;
}

void insertionSort(int arr[], int size) {
	int idx = 1;
	// idx는 1부터 시작한다.
	// size인 7보다 작을 때 까지 while문을 반복한다.
	while (idx < size) {
		// i는 0부터 (idx - 1)까지 반복하면서 값을 비교한다.
		for (int i = 0; i < idx; ++i) {
			// 만약 i번째 원소가 비교 하고 있었던 idx번째 원소보다 크다면
			if (arr[i] > arr[idx]) {
				// temp에 처음 비교를 시작했던 idx번재 원소를 저장해주고
				int temp = arr[idx];
				// idx부터 i까지 1씩 줄여가면서 값을 뒤로 한칸씩 미뤄준다.
				for (int j = idx - 1; j >= i; --j) {
					arr[j + 1] = arr[j];
				}
				// i번째 방에 temp를 넣어준다.
				arr[i] = temp;
				break;
			}
		}

		++idx;
	}

}