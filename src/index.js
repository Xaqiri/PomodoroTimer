const defaultBreak = 5
const defaultWork = 25
const changeAudio = (task, audio) => {
	audio = task === 'work' ? 'takeABreakAudio' : 'backToWorkAudio'
	return audio
}

$(document).ready(() => {
	let audio
	// Using the Work Timer and Break Timer buttons to change the displayed time
	$('#workTimerButton').click(() => {
		audio = changeAudio('work', audio)
		$('#stopButton').click()
		$('#minutes').text($('#workTime').text())
		$('#seconds').text('00')
	})
	$('#breakTimerButton').click(() => {
		audio = changeAudio('break', audio)
		$('#stopButton').click()
		$('#minutes').text($('#breakTime').text())
		$('#seconds').text('00')
	})

	// Use the Start and Stop buttons for the timer
	let timer
	$('#startButton').click(() => {
		timer = setInterval(() => {
			let seconds = parseInt($('#seconds').text())
			let minutes = parseInt($('#minutes').text())
			if (seconds - 1 >= 0) {
				seconds--
			} else {
				seconds = 5
				minutes = minutes - 1 > 0 ? minutes - 1 : 0
			}
			seconds = seconds < 10 ? '0'+seconds : seconds
			$('#seconds').text(seconds)
			$('#minutes').text(minutes)
			if ($('#minutes').text() == 0 && $('#seconds').text() == 0) {
				$('#stopButton').click()
				document.getElementById(audio).play()
			}
		}, 1000)
	})
	$('#stopButton').click(() => {
		clearInterval(timer)
	})
	// Setting the length of the timers
	$('#set_break div').first().click(() => {
		$('#breakTime').text(defaultBreak)
		$('#breakTimerButton').click()
	})
	$('#breakMinus').click(() => {
		let breakTime = $('#breakTime').text()
		breakTime = breakTime - 1 > 1 ? breakTime - 1 : 1
		$('#breakTime').text(breakTime)
		$('#breakTimerButton').click()
	})
	$('#breakPlus').click(() => {
		let breakTime = parseInt($('#breakTime').text())
		breakTime = breakTime + 1 < 60 ? breakTime + 1 : 60
		$('#breakTime').text(breakTime)
		$('#breakTimerButton').click()
	})
	$('#set_work div').first().click(() => {
		$('#workTime').text(defaultWork)
		$('#workTimerButton').click()
	})
	$('#workMinus').click(() => {
		let workTime = $('#workTime').text()
		workTime = workTime - 1 > 1 ? workTime - 1 : 1
		$('#workTime').text(workTime)
		$('#workTimerButton').click()
	})
	$('#workPlus').click(() => {
		let workTime = parseInt($('#workTime').text())
		workTime = workTime + 1 < 60 ? workTime + 1 : 60
		$('#workTime').text(workTime)
		$('#workTimerButton').click()
	})
})
