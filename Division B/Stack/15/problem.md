<div class="problem-statement">
   <div class="header">
      <h1 class="title">15. Великое Лайнландское переселение</h1>
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
   <div class="legend"> Лайнландия представляет из себя одномерный мир, являющийся прямой, на котором располагаются N городов, последовательно пронумерованных
      от 0 до N - 1 . Направление в сторону от первого города к нулевому названо западным, а в обратную&nbsp;— восточным. <!--l.
      49-->
      <p style="text-indent: 0em;">Когда в Лайнландии неожиданно начался кризис, все были жители мира стали испытывать глубокое
      смятение. По всей Лайнландии стали ходить слухи, что на востоке живётся лучше, чем на западе. <!--l. 51-->
      </p><p style="text-indent: 0em;">Так и началось Великое Лайнландское переселение. Обитатели мира целыми городами отправились
      на восток, покинув родные улицы, и двигались до тех пор, пока не приходили в город, в котором средняя цена проживания была
      меньше, чем в родном. </p>
      <p></p>
      
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> В первой строке дано одно число N (<!--l. 54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn>
      <mo>≤</mo> <mi>N</mi> <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>5</mn></mrow></msup></math>)&nbsp;— количество
      городов в Лайнландии. Во второй строке дано N чисел <!--l. 54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><msub><mrow><mi>a</mi></mrow><mrow><mi>i</mi></mrow></msub></math>
      (<!--l. 54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn> <mo>≤</mo>
      <msub><mrow><mi>a</mi></mrow><mrow><mi>i</mi></mrow></msub> <mo>≤</mo> <mn>1</mn><msup><mrow><mn>0</mn></mrow><mrow><mn>9</mn></mrow></msup></math>)&nbsp;—
      средняя цена проживания в городах с нулевого по (N - 1)-ый соответственно. 
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Для каждого города в порядке с нулевого по (N - 1)-ый выведите номер города, в который переселятся его изначальные жители.
      Если жители города не остановятся в каком-либо другом городе, отправившись в Восточное Бесконечное Ничто, выведите -1 . 
   </div>
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
            <td><pre>10
1 2 3 2 1 4 2 5 3 1
</pre></td>
            <td><pre>-1 4 3 4 -1 6 9 8 9 -1
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
