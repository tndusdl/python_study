import pandas as pd

data = {'이름': ['Kim', 'Park', 'Lee', 'Ho'],
        '국어': [90, 58, 88, 100],
        '영어': [100, 60, 80, 70],
        '수학': [55, 65, 76, 88] }

df = pd.DataFrame(data)

# 1에서 만든 데이터 프레임 출력하기
print(df, end='\n\n')

# 학생 이름만 추출해서 출력하기 (열 추출)
sr_name = df['이름']
print(sr_name, end='\n\n')

# 'Park' 성적만 출력하기
park_data = df.loc[1]

# 'Ho' 학생의 수학점수를 90점으로 수정하기
df.loc[df['이름'] == 'Ho', '수학'] = 90
print(df, end='\n\n')

# 'Oh' 학생의 국어(100), 영어(70), 수학(80) 성적을 새로 추가하기
df.loc[3] = ['Oh', 100, 70, 80]
print(df, end='\n\n')

# 'Lee' 학생의 성적을 삭제하기
df = df.drop([2], axis=0)
print(df, end='\n\n')
