/*
* 22/08/14
* Oh Jin Young
*/
#include <stdlib.h>
#include <stdio.h>

int map[9][9] = { 0 };  //스도쿠 판을 담을 2차원 배열 map
int zero_cnt = 0;       //스도쿠에서 0이 들어있는(우리가 채워 넣어야하는) 갯수를 담을 zero_cnt 변수

/*
* 
* 인자 : 
*   int num : 스도쿠판에서 어느 위치의 값을 볼것인지 위치를 나타내주는 num변수
*             스도쿠의 판이 9 X 9로 총 81칸이 있으니 왼쪽 위에서부터 각 스도쿠 판의 위치를
*             0 ~ 80까지 총 81개의 숫자로 표현을 해줄 것임
* 설명 : 
*   스도쿠의 판을 하나씩 돌면서 우리가 채워 넣어야하는 0에 값을 넣어줄 check함수
* 
*/
void dfs(int num) {
    int col = num % 9;     //num을 바탕으로 column(열) 값을 구해서 담아줄 col변수
    int row = num / 9;     //num을 바탕으로 row(행) 값을 구해서 담아줄 row변수

    //만약 스도쿠 내에 빈칸을 다 채운 경우 실행
    if (zero_cnt == 0) {
        //정답 스도쿠판을 출력해줌
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                printf("%d ", map[i][j]);
            }
            printf("\n");
        }
        exit(0);    //프로그램 종료
    }

    //해당 칸이 비어있는 경우 실행
    if (map[row][col] == 0) {
        bool is_in[10] = { false }; // 1~9의 숫자가 해당 칸에 영향을 끼치는 요소(가로줄, 세로줄, 3x3사각형의 구역)들중에 얼마나 들어있는지 check할 is_in배열
        int rl_box = col / 3;       // box 구역을 나타낼때 사용할 변수
        int updown_box = row / 3;   // box 구역을 나타낼때 사용할 변수

        // 3x3 정사각형 9칸안에서 들어있는 숫자들을 is_in에 check해줌(true로 바꿔줌)
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (map[updown_box * 3 + i][rl_box * 3 + j] != 0) {
                    is_in[map[updown_box * 3 + i][rl_box * 3 + j]] = true;
                }
            }
        }

        //가로줄, 세로줄에서 들어있는 숫자들을 check해줌
        for (int i = 0; i < 9; i++) {
            is_in[map[row][i]] = true;
            is_in[map[i][col]] = true;
        }

        //해당 칸에 들어갈 수 있는 1~9의 값을 넣어줌
        for (int i = 1; i <= 9; i++) {
            if (!is_in[i]) {
                map[row][col] = i;  //해당 칸에 들어갈 수 있는 값을 넣어줌
                zero_cnt--;         //하나의 값을 채워줬으니 zero_cnt를 줄여줌
                dfs((num + 1) % 81);  //다음칸으로 넘어감
                //이 아래로 나온거면 위에서 채운 값을 넣었을 때 답이 나오지 않은 경우임
                map[row][col] = 0;  //해당 칸을 다시 비워줌
                zero_cnt++;         //하나의 값을 채웠다가 다시 뺐으니 zero_cnt를 올려줌
            }
        }
    }
    else {  //해당 칸이 비어있지 않다면 다음 칸으로 넘어감
        dfs((num + 1) % 81);  
    }
}

int main() {
    //사용자로부터 스도쿠 판 정보를 받고 map에 넣어주면서 0의 갯수 (빈칸의 갯수)를 셈
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            scanf("%d", &map[i][j]);
            if (map[i][j] == 0)  zero_cnt++;
        }
    }

    dfs(0);   //스도쿠의 0번째 칸(맨 왼쪽 위의 칸)부터 돌면서 정답 스도쿠를 찾아감

    return 0;
}