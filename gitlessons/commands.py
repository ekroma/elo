GIT - распределенная система контроля версий (Это система для отслеживания и ведения истории изменений ваших файлов или проектов)

РЕПОЗИТОРИЙ - Это хранилище ваших файлов, которые вы отслеживаете при помощи гита, и их изменений.

КОМАНДЫ GIT:

1. git init - Она создает новый гит репозиторий на вашем пк. создаст она в том дериктории где вы запускаете эту команду.

2. git add - Когда мы создаем и изменяем файлы, то при помощи это команды мы загружаем все изменения в промежуточное место хранение

git add <file name>
git add . -> все в текущий файл

3. git commit - как только мы достигаем определенного момента разроботки то мы тогда сохраняем и комментируем все наши изменения в репозиторий.
(фиксация изменений а репо.)

git commit -m '<comment>'

4. git remote add - это команда для того чтобы связать ваш локальный репозиторий с удаленныйм репозиторием(репо в гитхабе)
git remote add <название подключения> <ссылка на репозиторий>

git remote add origin <url>

5. git push - после коммита изменений при помощи этой команды мы отправляем наш изменения в файлах на удаленнный репозиторий 

git push <origin> <название ветки(main)>

git push origin main

--------------------------------------------------------------------------

1. git init
2. git branch -M main (переименовываем глав ветку с мастер с master на main)
3. git add .
4. gitt commit -m 'comment' (добавлено в локал репо)
5. git remote add origin <url>
6. git push origin main

//////////////////////

git add .
git commit -m 'commrnt'
git push origin main

-------------------------------

