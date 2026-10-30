let quizData = [];
function generate(){
  const topic = document.getElementById('topic').value || 'html';
  const T = topic.toUpperCase();
  let flashcards = [];
  for(let i=1; i<=10; i++){
    flashcards.push({question: `${i}. What is ${topic} - Concept ${i}?`, answer: `${T} is very important concept. ${topic} helps to learn basics and advanced topics with real examples. Students who learn ${topic} can build projects and score high marks. This is foundation topic for college students.`});
  }
  let quiz = [];
  for(let i=1; i<=10; i++){
    quiz.push({question: `${i}. Which is TRUE about ${topic}?`, options: [`${topic} is useful`, `${topic} is useless`, "Both are wrong", "None of these"], answer: `${topic} is useful`});
  }
  document.getElementById('fc').innerText = '10 Cards';
  document.getElementById('qc').innerText = '10 Questions';
  document.getElementById('flashcards').innerHTML = flashcards.map(c=>`<div class="card"><b>${c.question}</b><p>${c.answer}</p></div>`).join('');
  quizData = quiz;
  document.getElementById('quiz').innerHTML = quiz.map((q,i)=>`<div class="card"><b>${q.question}</b><br>${q.options.map(o=>`<label><input type="radio" name="q${i}" value="${o}"> ${o}</label><br>`).join('')}</div>`).join('');
  document.getElementById('result').innerHTML = '<p style="color:green">✅ Generated Successfully - 10 Cards!</p>';
}
function submitQuiz(){
  let s=0; quizData.forEach((q,i)=>{const sel=document.querySelector(`input[name="q${i}"]:checked`); if(sel && sel.value===q.answer) s++;});
  document.getElementById('result').innerHTML = `<h2>Your Score: ${s} / 10</h2>`;
}