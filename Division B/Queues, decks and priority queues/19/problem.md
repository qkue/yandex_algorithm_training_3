<div class="problem-statement">
   <div class="header">
      <h1 class="title">19. Хипуй</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>2&nbsp;секунды</td>
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
         <p>В этой задаче вам необходимо самостоятельно (не используя соответствующие классы и функции стандартной библиотеки) организовать
            структуру данных Heap для хранения целых чисел, над которой определены следующие операции: a) Insert(k) – добавить в Heap
            число k ; b) Extract достать из Heap наибольшее число (удалив его при этом).
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке содержится количество команд N (1 ≤ N ≤ 100000), далее следуют N команд, каждая в своей строке. Команда может
            иметь формат: “0 &lt;число&gt;” или “1”, обозначающий, соответственно, операции Insert(&lt;число&gt;) и Extract. Гарантируется, что при
            выполнении команды Extract в структуре находится по крайней мере один элемент.
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Для каждой команды извлечения необходимо отдельной строкой вывести число, полученное при выполнении команды Extract. </p></span><p></p>
   </div>
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
            <td><pre>2
0 10000
1
</pre></td>
            <td><pre>10000
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
            <td><pre>14
0 1
0 345
1
0 4346
1
0 2435
1
0 235
0 5
0 365
1
1
1
1
</pre></td>
            <td><pre>345
4346
2435
365
235
5
1
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
