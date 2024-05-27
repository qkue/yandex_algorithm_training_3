<div class="problem__statement text" data-bem="{&quot;problem__statement&quot;:{}}">
<div class="problem-statement">
   <div class="header">
      <h1 class="title">24. Покупка билетов</h1>
      <table>
         <tbody><tr class="time-limit">
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
      </tbody></table>
   </div>
   <h2></h2>
   <div class="legend"><span style="">
         <p>За билетами на премьеру нового мюзикла выстроилась очередь из N человек, каждый из которых хочет купить 1 билет. На всю очередь
            работала только одна касса, поэтому продажа билетов шла очень медленно, приводя «постояльцев» очереди в отчаяние. Самые сообразительные
            быстро заметили, что, как правило, несколько билетов в одни руки кассир продаёт быстрее, чем когда эти же билеты продаются
            по одному. Поэтому они предложили нескольким подряд стоящим людям отдавать деньги первому из них, чтобы он купил билеты на
            всех.
         </p></span><p>Однако для борьбы со спекулянтами кассир продавала не более 3-х билетов в одни руки, поэтому договориться таким образом между
         собой могли лишь 2 или 3 подряд стоящих человека.
      </p>
      <p>Известно, что на продажу i-му человеку из очереди одного билета кассир тратит <span class="tex-math-text">A<sub>i</sub></span> секунд, на продажу двух билетов — <span class="tex-math-text">B<sub>i</sub></span> секунд, трех билетов — <span class="tex-math-text">C<sub>i</sub></span> секунд. Напишите программу, которая подсчитает минимальное время, за которое могли быть обслужены все покупатели.
      </p>
      <p>Обратите внимание, что билеты на группу объединившихся людей всегда покупает первый из них. Также никто в целях ускорения
         не покупает лишних билетов (то есть билетов, которые никому не нужны).
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>На вход программы поступает сначала число N — количество покупателей в очереди (1 ≤ N ≤ 5000). Далее идет N троек натуральных
            чисел <span class="tex-math-text">A<sub>i</sub></span>, <span class="tex-math-text">B<sub>i</sub></span>, <span class="tex-math-text">C<sub>i</sub></span>. Каждое из этих чисел не превышает 3600. Люди в очереди нумеруются, начиная от кассы.
         </p></span><p></p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Требуется вывести одно число — минимальное время в секундах, за которое могли быть обслужены все покупатели.</p></span><p></p>
   </div>
   <h2>Пример</h2>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод<div class="problem__copy-sample"><button class="button button_theme_pseudo button_size_s button_only-icon_yes problem__copy-button problem__copy-button_type_input i-bem" data-bem="{&quot;button&quot;:{}}" role="button" type="button" title="Скопировать ввод"><span class="button__text">&nbsp;<img class="image button__icon button__icon_role_copy" src="//yastatic.net/lego/_/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif" alt="Скопировать ввод"></span></button></div></th>
            <th>Вывод<div class="problem__copy-sample"><button class="button button_theme_pseudo button_size_s button_only-icon_yes problem__copy-button problem__copy-button_type_output i-bem" data-bem="{&quot;button&quot;:{}}" role="button" type="button" title="Скопировать вывод"><span class="button__text">&nbsp;<img class="image button__icon button__icon_role_copy" src="//yastatic.net/lego/_/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif" alt="Скопировать вывод"></span></button></div></th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>5
5 10 15
2 10 15
5 5 5
20 20 1
20 1 1
</pre></td>
            <td><pre>12
</pre></td>
         </tr>
      </tbody>
   </table>
</div></div>
