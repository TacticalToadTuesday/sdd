// HTML elements
const behaviourSlider = document.getElementById('behaviour');
const attendanceSlider = document.getElementById('attendance');
const gradesSlider = document.getElementById('grades');

const behaviourLabel = document.getElementById('behaviourLabel');
const attendanceLabel = document.getElementById('attendanceLabel');
const gradesLabel = document.getElementById('gradesLabel');

// Event listeners for slider changes
behaviourSlider.addEventListener('input', updateBehaviourLabel);
attendanceSlider.addEventListener('input', updateAttendanceLabel);
gradesSlider.addEventListener('input', updateGradesLabel);

// Function to update behaviour label
function updateBehaviourLabel() {
  const behaviourValue = parseInt(behaviourSlider.value);
  behaviourLabel.textContent = Behaviour(behaviourValue);
}

// Function to update attendance label
function updateAttendanceLabel() {
  const attendanceValue = parseInt(attendanceSlider.value);
  attendanceLabel.textContent = Attendance(attendanceValue);
}

// Function to update grades label
function updateGradesLabel() {
  const gradesValue = parseInt(gradesSlider.value);
  gradesLabel.textContent = Grades(gradesValue);
}

function Behaviour(value) {
  let labelValue = '';
  switch (value) {
    case 1:
      labelValue = 'Disruptive';
      break;
    case 2:
      labelValue = 'Inattentive';
      break;
    case 3:
      labelValue = 'Inconsistent';
      break;
    case 4:
      labelValue = 'Passive';
      break;
    case 5:
      labelValue = 'Cooperative';
      break;
    case 6:
      labelValue = 'Engaged';
      break;
    case 7:
      labelValue = 'Exemplary';
      break;
    default:
      labelValue = '';
  }
  return labelValue;
}

function Attendance(value) {
  let labelValue = '';
  switch (value) {
    case 1:
      labelValue = 'Absentee';
      break;
    case 2:
      labelValue = 'Irregular';
      break;
    case 3:
      labelValue = 'Sporadic';
      break;
    case 4:
      labelValue = 'Tardy';
      break;
    case 5:
      labelValue = 'Adequate';
      break;
    case 6:
      labelValue = 'Punctual';
      break;
    case 7:
      labelValue = 'Exceptional';
      break;
    default:
      labelValue = '';
  }
  return labelValue;
}

function Grades(value) {
  let labelValue = '';
  switch (value) {
    case 1:
      labelValue = 'Failing';
      break;
    case 2:
      labelValue = 'Poor';
      break;
    case 3:
      labelValue = 'Mediocre';
      break;
    case 4:
      labelValue = 'Average';
      break;
    case 5:
      labelValue = 'Satisfactory';
      break;
    case 6:
      labelValue = 'Good';
      break;
    case 7:
      labelValue = 'Excellent';
      break;
    default:
      labelValue = '';
  }
  return labelValue;
}