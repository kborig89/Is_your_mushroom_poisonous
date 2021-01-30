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
  shuffledQuestions = questions.sort(() => Math.random() - .5)
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

      { text: 'Bell', correct: true },
      { text: 'Conical', correct: true },
      { text: 'Convex', correct: true },
      { text: 'Flat', correct: true },
      { text: 'Sunken', correct: true },
      { text: 'Knobbed', correct: true }
    ]
  },
  {
    question: 'Cap Surface?',
    answers: [

      { text: 'Fibrous', correct: true },
      { text: 'Grooves', correct: true },
      { text: 'Scaly', correct: true },
      { text: 'Smooth', correct: true }
    ]
  },
  {
    question: 'Cap Color?',
    answers: [ 

      { text: 'Brown', correct: true },
      { text: 'Buff', correct: true },
      { text: 'Binnamon', correct: true },
      { text: 'Gray', correct: true },
      { text: 'Green', correct: true },
      { text: 'Pink', correct: true },
      { text: 'Purple', correct: true },
      { text: 'Red', correct: true },
      { text: 'White', correct: true },
      {text: 'Yellow', correct: true }
    ]
  },
  {
    question: 'What is Odor Like?',
    answers: [

      { text: 'Almond', correct: true },
      { text: 'Anise', correct: true },
      { text: 'Creosote', correct: true },
      { text: 'Fishy', correct: true },
      { text: 'Foul', correct: true },
      { text: 'Musty', correct: true },
      { text: 'None', correct: true },
      { text: 'Pungent', correct: true },
      {text: 'Spicy', correct: true }

    ]
  },
  {
    question: 'What is the Spore Print Color?',
    answers: [

      { text: 'Black', correct: true },
      { text: 'Brown', correct: true },
      { text: 'Buff', correct: true },
      { text: 'Chocolate', correct: true },
      { text: 'Green', correct: true },
      { text: 'Orange', correct: true },
      { text: 'Purple', correct: true },
      { text: 'White', correct: true },
      {text: 'Yellow', correct: true }
    ]
  }
]