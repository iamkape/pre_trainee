import pandas as pd
import numpy as np
pd.options.display.max_columns = None


df = pd.read_csv("./data_files/adult.data.csv")
pd.options.display.max_columns = None


#1. Посчитайте, сколько мужчин и женщин (признак sex) представлено в этом датасете

print(df.groupby('sex')['age'].count().reset_index(name='Количество'))


#2. Каков средний возраст мужчин (признак age) по всему датасету?

print(df.groupby('sex')['age'].mean().tail(1).reset_index(name='Средний возвраст мужчин'))


#3. Какова доля граждан Соединенных Штатов (признак native-country)?

test_percent_native = df['native-country'].value_counts(normalize=True).head(1).reset_index(name='Доля граждан')
print(test_percent_native)


#4-5. Рассчитайте среднее значение и среднеквадратичное отклонение возраста тех,
# кто получает более 50K в год (признак salary) и тех, кто получает менее 50K в год

print(df.loc[df['salary']=='>50K', 'age'].agg(['mean', 'std']).reset_index(name='>50K'))
print(df.loc[df['salary']=='<=50K', 'age'].agg(['mean', 'std']).reset_index(name='<=50K'))


#6. Правда ли, что люди, которые получают больше 50k, имеют минимум высшее образование?
# (признак education – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters или Doctorate)

print(df.loc[df['salary']=='>50K', 'education'].isin(['Bachelors',
                                                'Prof-school',
                                                'Assoc-acdm',
                                                'Assoc-voc',
                                                'Masters',
                                                'Doctorate']).reset_index(name='Есть ли высшее'))


#7. Выведите статистику возраста для каждой расы (признак race) и каждого пола.
# Используйте groupby и describe. Найдите таким образом максимальный возраст мужчин расы Asian-Pac-Islander.

print(df.groupby(['race','sex'])['age'].describe()) # статистика
print(df[(df['race']=='Asian-Pac-Islander') & (df['sex']=='Male')]['age'].max())


#8. Среди кого больше доля зарабатывающих много (>50K): среди женатых или холостых мужчин (признак marital-status)?
# Женатыми считаем тех, у кого marital-status начинается с Married
# (Married-civ-spouse, Married-spouse-absent или Married-AF-spouse), остальных считаем холостыми.

family_status = df.loc[df['salary']=='>50K', 'marital-status'].isin(['Married-civ-spouse',
                                                           'Married-spouse-absent',
                                                           'Married-AF-spouse'])
print(family_status.replace({True: 'Женатых',
                             False: 'Холостых'}).value_counts().reset_index(name='Кол-во'))


#9. Какое максимальное число часов человек работает в неделю (признак hours-per-week)?
# Сколько людей работают такое количество часов и каков среди них процент зарабатывающих много?

max_hours = df['hours-per-week'].max() # Максимальное число рабочих часов
work_numb = df[df['hours-per-week'] == max_hours].shape[0] # Количество человек работающих масимальные часы.
print((df[(df['salary']=='>50K') & (df['hours-per-week'] == max_hours)].shape[0] / work_numb *100))


#10. Посчитайте среднее время работы (hours-per-week) зарабатывающих
# мало и много (salary) для каждой страны (native-country).

print(df.groupby(['native-country', 'salary'])['hours-per-week'].mean().unstack())


# 11.Сгруппируйте людей по возрастным группам young, adult, retiree, где:
#
# young соответствует 16-35 лет
# adult - 35-70 лет
# retiree - 70-100 лет
# Проставьте название соответсвтуещей группы для каждого человека в новой колонке AgeGroup
conditions = [ (df['age'] > 16) & (df['age'] < 35),
               (df['age'] > 35) & (df['age'] < 70),
               (df['age'] > 70) & (df['age'] < 100)
               ]
age_status = ['young', 'adult', 'retiree']
df['AgeGroup'] = np.select(conditions, age_status, default='None')
print(df)


#12-13. Определите количество зарабатывающих >50K в каждой из возрастных групп (колонка AgeGroup),
# а также выведите название возрастной группы, в которой чаще зарабатывают больше 50К (>50K)

salary_50 = df.loc[df['salary']=='>50K', 'AgeGroup'].value_counts()
print(salary_50)
rich_age_group = df.loc[df['salary']=='>50K', 'AgeGroup']
print(rich_age_group.value_counts().idxmax())


#14. Сгруппируйте людей по типу занятости (колонка occupation) и определите количество людей в каждой группе.
# После чего напишите функциюю фильтрации filter_func, которая будет возвращать только те группы,
# в которых средний возраст (колонка age) не больше 40 и в которых все работники отрабатывают более 5 часов в неделю
# (колонка hours-per-week)

occupation_group = df.groupby('occupation').count()
print(occupation_group)

def filter_func(dataframe):
    return  dataframe.filter(lambda x: x['age'].mean() <= 40 and (x['hours-per-week'] > 5).all())
grouped = df.groupby('occupation')
print(filter_func(grouped))