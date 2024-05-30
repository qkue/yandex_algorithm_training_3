<div class="problem-statement">
   <div class="header">
      <h1 class="title">26. Самый дешевый путь</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>1&nbsp;секунда</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>256Mb</td>
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
   <div class="legend"> В каждой клетке прямоугольной таблицы <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi>
      <mo>×</mo> <mi>M</mi></math> записано некоторое число. Изначально игрок находится в левой верхней клетке. За один ход ему
      разрешается перемещаться в соседнюю клетку либо вправо, либо вниз (влево и вверх перемещаться запрещено). При проходе через
      клетку с игрока берут столько килограммов еды, какое число записано в этой клетке (еду берут также за первую и последнюю клетки
      его пути). <!--l. 49-->
      <p style="text-indent: 0em;">Требуется найти минимальный вес еды в килограммах, отдав которую игрок может попасть в правый
      нижний угол. </p>
      
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> Вводятся два числа N и M&nbsp;— размеры таблицы (<!--l. 52--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn>
      <mo>≤</mo> <mi>N</mi> <mo>≤</mo> <mn>2</mn><mn>0</mn></math>, <!--l. 52--><math display="inline" style="text-indent: 0em;"
      xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>≤</mo> <mi>M</mi> <mo>≤</mo> <mn>2</mn><mn>0</mn></math>). Затем
      идет N строк по M чисел в каждой&nbsp;— размеры штрафов в килограммах за прохождение через соответствующие клетки (числа от
      0 до 100). 
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Выведите минимальный вес еды в килограммах, отдав которую можно попасть в правый нижний угол. </div>
   <h2>Пример</h2>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>5 5
1 1 1 1 1
3 100 100 100 100
1 1 1 1 1
2 2 2 2 1
1 1 1 1 1
</pre></td>
            <td><pre>11
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
