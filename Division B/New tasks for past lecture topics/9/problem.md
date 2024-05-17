<div class="problem-statement">
   <div class="header">
      <h1 class="title">9. Сумма в прямоугольнике</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>3&nbsp;секунды</td>
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
   <div class="legend"><span style="">
         <p>Вам необходимо ответить на запросы узнать сумму всех элементов числовой матрицы N×M в прямоугольнике с левым верхним углом
            (<span class="tex-math-text">x<sub>1</sub>, y<sub>1</sub></span>) и правым нижним (<span class="tex-math-text">x<sub>2</sub>, y<sub>2</sub></span>)
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке находится числа N, M размеры матрицы (<span class="tex-math-text">1 &le; N, M &le; 1000</span>) и K&nbsp;&mdash; количество запросов (<span class="tex-math-text">1 &le; K &le; 100000</span>). Каждая из следующих N строк содержит по M чисел`&mdash; элементы соответствующей строки матрицы (по модулю не превосходят 1000). Последующие K строк содержат по 4 целых числа, разделенных
            пробелом <span class="tex-math-text">x<sub>1</sub> y<sub>1</sub> x<sub>2</sub> y<sub>2</sub></span>&nbsp;&mdash; запрос на сумму элементов матрице в прямоугольнике (<span class="tex-math-text">1 &le; x<sub>1</sub> &le; x<sub>2</sub> &le; N</span>, <span class="tex-math-text">1 &le; y<sub>1</sub> &le; y<sub>2</sub> &le; M</span>)
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Для каждого запроса на отдельной строке выведите его результат&nbsp;&mdash; сумму всех чисел в элементов матрице в прямоугольнике (<span class="tex-math-text">x<sub>1</sub>, y<sub>1</sub></span>), (<span class="tex-math-text">x<sub>2</sub>, y<sub>2</sub></span>)
         </p></span></div>
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
            <td><pre>3 3 2
1 2 3
4 5 6
7 8 9
2 2 3 3
1 1 2 3
</pre></td>
            <td><pre>28
21
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
