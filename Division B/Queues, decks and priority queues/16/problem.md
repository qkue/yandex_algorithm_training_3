<div class="problem-statement">
   <div class="header">
      <h1 class="title">16. Очередь с защитой от ошибок</h1>
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
         <p>Научитесь пользоваться стандартной структурой данных queue для целых чисел. Напишите программу, содержащую описание очереди
            и моделирующую работу очереди, реализовав все указанные здесь методы.&nbsp; 
         </p></span><p>Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. После выполнения&nbsp;каждой
         команды программа должна вывести одну строчку. 
      </p>
      <p>Возможные команды для программы: </p>
      <p>push n<br> Добавить в очередь число n (значение n задается после команды). Программа должна вывести ok. 
      </p>
      <p>pop<br> Удалить из очереди первый элемент. Программа должна вывести его значение. 
      </p>
      <p>front<br> Программа должна вывести значение первого элемента, не удаляя его из очереди. 
      </p>
      <p>size<br> Программа должна вывести количество элементов в очереди. 
      </p>
      <p>clear<br> Программа должна очистить очередь и вывести ok. 
      </p>
      <p>exit<br> Программа должна вывести bye и завершить работу. 
      </p>
      <p>Перед исполнением операций front и pop программа должна проверять, содержится ли в очереди хотя бы один элемент. Если во входных
         данных встречается операция front или pop, и при этом очередь пуста, то программа должна вместо числового значения вывести
         строку error. 
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Вводятся команды управления очередью, по одной на строке </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Требуется вывести протокол работы очереди, по одному сообщению на строке </p></span></div>
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
            <td><pre>push 1
front
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
push 1
size
push 2
size
push 3
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
            <td><pre>push 3
push 14
size
clear
push 1
front
push 2
front
pop
size
pop
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
1
1
2
0
bye
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
