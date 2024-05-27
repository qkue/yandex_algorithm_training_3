<div class="problem-statement">
   <div class="header">
      <h1 class="title">18. Дек с защитой от ошибок</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>1&nbsp;секунда</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>64Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="1">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="1">стандартный вывод или output.txt</td>
         </tr>
      </table>
   </div>
   <h2></h2>
   <div class="legend"><span style="">
         <p>Научитесь пользоваться стандартной структурой данных deque для целых чисел.&nbsp; Напишите программу, содержащую описание дека
            и моделирующую работу дека, реализовав все указанные здесь методы. Программа считывает последовательность команд и в зависимости
            от команды выполняет ту или иную операцию. После выполнения&nbsp;каждой команды программа должна вывести одну строчку. 
         </p></span><p>Возможные команды для программы: </p>
      <p>push_front n<br> Добавить (положить) в начало дека новый элемент. Программа должна вывести ok. 
      </p>
      <p>push_back n<br> Добавить (положить) в конец дека новый элемент. Программа должна вывести ok. 
      </p>
      <p>pop_front<br> Извлечь из дека первый элемент. Программа должна вывести его значение. 
      </p>
      <p>pop_back<br> Извлечь из дека последний элемент. Программа должна вывести его значение. 
      </p>
      <p>front<br> Узнать значение первого элемента (не удаляя его). Программа должна вывести его значение. 
      </p>
      <p>back<br> Узнать значение последнего элемента (не удаляя его). Программа должна вывести его значение. 
      </p>
      <p>size<br> Вывести количество элементов в деке. 
      </p>
      <p>clear<br> Очистить дек (удалить из него все элементы) и вывести ok. 
      </p>
      <p>exit<br> Программа должна вывести bye и завершить работу. 
      </p>
      <p>Гарантируется, что количество элементов в деке в любой момент не превосходит 100. Перед исполнением операций pop_front, pop_back,
         front, back программа должна проверять, содержится ли в деке хотя бы один элемент. Если во входных данных встречается операция
         pop_front, pop_back, front, back, и&nbsp;при этом дек пуст, то программа должна вместо числового значения вывести строку error.
         
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Вводятся команды управления деком, по одной на строке. </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Требуется вывести протокол работы дека, по одному сообщению на строке </p></span></div>
   <h3>Пример 1</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>push_back 1
back
exit
</pre></td>
            <td><pre>ok
1
bye
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 2</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>size
push_back 1
size
push_back 2
size
push_front 3
size
exit
</pre></td>
            <td><pre>0
ok
1
ok
2
ok
3
bye
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 3</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>push_back 3
push_front 14
size
clear
push_front 1
back
push_back 2
front
pop_back
size
pop_front
size
exit
</pre></td>
            <td><pre>ok
ok
2
ok
ok
1
ok
1
2
1
1
0
bye
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
