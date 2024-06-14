<div class="problem-statement">
   <div class="header">
      <h1 class="title">33. Списывание</h1>
      <table>
         <thead>
            <th></th>
            <th>Все языки</th>
            <th>Python 3.6</th>
         </thead>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>2&nbsp;секунды</td>
            <td>5&nbsp;секунд</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>256Mb</td>
            <td>256Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="2">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="2">стандартный вывод или output.txt</td>
         </tr>
      </table>
   </div>
   <h2></h2>
   <div class="legend"><span style="">
         <p>Во время контрольной работы профессор Флойд заметил, что некоторые студенты обмениваются записками. Сначала он хотел поставить
            им всем двойки, но в тот день профессор был добрым, а потому решил разделить студентов на две группы: списывающих и дающих
            списывать, и поставить двойки только первым. 
         </p></span><p>У профессора записаны все пары студентов, обменявшихся записками. Требуется определить, сможет ли он разделить студентов на
         две группы так, чтобы любой обмен записками осуществлялся от студента одной группы студенту другой группы.
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке находятся два числа <span class="tex-math-text">N</span> и <span class="tex-math-text">M</span>&nbsp;&mdash; количество студентов и количество пар студентов, обменивающихся записками (<span class="tex-math-text">1 &le; N &le; 10<sup>2</sup></span>, <span class="tex-math-text">0 &le; M &le; N(N−1)/2</span>). 
         </p></span><p>Далее в <span class="tex-math-text">M</span> строках расположены описания пар студентов: два числа, соответствующие номерам студентов, обменивающихся записками (нумерация
         студентов идёт с <span class="tex-math-text">1</span>). Каждая пара студентов перечислена не более одного раза. 
      </p>
      <p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Необходимо вывести ответ на задачу профессора Флойда. Если возможно разделить студентов на две группы - выведите YES; иначе
            выведите NO.
         </p></span></div>
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
            <td><pre>3 2
1 2
2 3
</pre></td>
            <td><pre>YES
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
            <td><pre>3 3
1 2
2 3
1 3
</pre></td>
            <td><pre>NO
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
