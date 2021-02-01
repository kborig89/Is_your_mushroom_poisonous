const startButton = document.getElementById('start-btn')
const nextButton = document.getElementById('next-btn')
const questionContainerElement = document.getElementById('question-container')
const questionElement = document.getElementById('question')
const answerButtonsElement = document.getElementById('answer-buttons')

let shuffledQuestions, currentQuestionIndex

startButton.addEventListener('click', startGame)
nextButton.addEventListener('click', () => {
  currentQuestionIndex++
  setNextQuestion()
})

function startGame() {
  startButton.classList.add('hide')
  shuffledQuestions = questions.sort()
  currentQuestionIndex = 0
  questionContainerElement.classList.remove('hide')
  setNextQuestion()
}
 
function setNextQuestion() {
  resetState()
  showQuestion(shuffledQuestions[currentQuestionIndex])
}

function showQuestion(question) {
  questionElement.innerText = question.question
  question.answers.forEach(answer => {
    const button = document.createElement('button')
    button.innerText = answer.text
    button.classList.add('btn')
    if (answer.correct) {
      button.dataset.correct = answer.correct
    }
    button.addEventListener('click', selectAnswer)
    answerButtonsElement.appendChild(button)
  })
}

function resetState() {
  clearStatusClass(document.body)
  nextButton.classList.add('hide')
  while (answerButtonsElement.firstChild) {
    answerButtonsElement.removeChild(answerButtonsElement.firstChild)
  }
}

function selectAnswer(e) {
  const selectedButton = e.target
  const correct = selectedButton.dataset.correct
  setStatusClass(document.body, correct)
  Array.from(answerButtonsElement.children).forEach(button => {
    setStatusClass(button, button.dataset.correct)
  })
  if (shuffledQuestions.length > currentQuestionIndex + 1) {
    nextButton.classList.remove('hide')
  } else {
    startButton.innerText = 'Restart'
    startButton.classList.remove('hide')
  }
}

function setStatusClass(element, correct) {
  clearStatusClass(element)
  if (correct) {
    element.classList.add('correct')
  } else {
    element.classList.add('wrong')
  }
}

function clearStatusClass(element) {
  element.classList.remove('correct')
  element.classList.remove('wrong')
}

const questions = [
  {
    question: 'What is the Cap Shape?',
    answers: [

      { text: 'Bell', correct: true ,value:"0"},
      { text: 'Conical', correct: true ,value:"1"},
      { text: 'Convex', correct: true ,value:"2"},
      { text: 'Flat', correct: true ,value:"3"},
      { text: 'Sunken', correct: true ,value:"4"},
      { text: 'Knobbed', correct: true ,value:"5"}
    ]
  },
  {
    question: 'Cap Surface?',
    answers: [

      { text: 'Fibrous', correct: true ,value:"0"},
      { text: 'Grooves', correct: true ,value:"1"},
      { text: 'Scaly', correct: true ,value:"2"},
      { text: 'Smooth', correct: true ,value:"3"}
    ]
  },
  {
    question: 'Cap Color?',
    answers: [ 

      { text: 'Brown', correct: true ,value:"0"},
      { text: 'Buff', correct: true ,value:"1"},
      { text: 'Binnamon', correct: true ,value:"2"},
      { text: 'Gray', correct: true ,value:"3"},
      { text: 'Green', correct: true ,value:"4"},
      { text: 'Pink', correct: true ,value:"5"},
      { text: 'Purple', correct: true ,value:"6"},
      { text: 'Red', correct: true ,value:"7"},
      { text: 'White', correct: true ,value:"8"},
      { text: 'Yellow', correct: true ,value:"9"}
    ]
  },
  {
    question: 'What is Odor Like?',
    answers: [

      { text: 'Almond', correct: true ,value:"0"},
      { text: 'Anise', correct: true ,value:"1"},
      { text: 'Creosote', correct: true ,value:"2"},
      { text: 'Fishy', correct: true ,value:"3"},
      { text: 'Foul', correct: true ,value:"4"},
      { text: 'Musty', correct: true ,value:"5"},
      { text: 'None', correct: true ,value:"6"},
      { text: 'Pungent', correct: true ,value:"7"},
      { text: 'Spicy', correct: true ,value:"8"}

    ]
  },
  {
    question: 'What is the Spore Print Color?',
    answers: [

      { text: 'Black', correct: true ,value:"0"},
      { text: 'Brown', correct: true ,value:"1"},
      { text: 'Buff', correct: true ,value:"2"},
      { text: 'Chocolate', correct: true ,value:"3"},
      { text: 'Green', correct: true ,value:"4"},
      { text: 'Orange', correct: true ,value:"5"},
      { text: 'Purple', correct: true ,value:"6"},
      { text: 'White', correct: true ,value:"7"},
      { text: 'Yellow', correct: true ,value:"8"}
    ]
  }
]