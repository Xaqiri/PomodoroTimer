$(document).ready(() => {
	let audio
	const defaultBreak = 5
	const defaultWork = 25
	const changeAudio = (task, audio) => {
		return task === 'work' ? 'takeABreakAudio' : 'backToWorkAudio'
	}
	const stop = () => {
		clearInterval(timer)
		$('#startStopButton').text('Start')
		timer = null
	}
	const decrementTimer = (buttonId) => {
		let time = parseInt($('#'+buttonId).text())
		time = time - 1 > 1 ? time - 1 : 1
		$('#'+buttonId).text(time)
		$('#'+buttonId+'Button').click()
	}
	const incrementTimer = (buttonId) => {
		let time = parseInt($('#'+buttonId).text())
		time = time + 1 < 60 ? time + 1 : 60
		$('#'+buttonId).text(time)
		$('#'+buttonId+'Button').click()
	}
	const changeDisplayedTime = (mode) => {
		audio = changeAudio(mode, audio)
		stop()
		$('#minutes').text($('#'+mode+'Time').text())
		$('#seconds').text('00')
	}
	const reinitializeTimer = () => {
		$('#workTime').text(defaultWork)
		$('#breakTime').text(defaultBreak)
		changeDisplayedTime('work')
	}

	// Using the Work Timer and Break Timer buttons to change the displayed time
	$('#workTimeButton').click(() => { changeDisplayedTime('work') })
	$('#breakTimeButton').click(() => { changeDisplayedTime('break') })

	// Changing the length of the timers
	$('#breakMinus').click(() => { decrementTimer('breakTime') })
	$('#breakPlus').click(() => { incrementTimer('breakTime') })
	$('#workMinus').click(() => { decrementTimer('workTime') })
	$('#workPlus').click(() => { incrementTimer('workTime') })
	$('#timer').click(() => { reinitializeTimer() })

	// Use the Start and Stop buttons for the timer
	let timer = null
	$('#startStopButton').click(() => {
		if (timer === null) {
			$('#startStopButton').text('Stop')
			timer = setInterval(() => {
				let seconds = parseInt($('#seconds').text())
				let minutes = parseInt($('#minutes').text())
				if (seconds - 1 >= 0) seconds--
				else {
					seconds = 59
					minutes = minutes - 1 > 0 ? minutes - 1 : 0
				}
				seconds = seconds < 10 ? '0'+seconds : seconds
				$('#seconds').text(seconds)
				$('#minutes').text(minutes)
				if ($('#minutes').text() == 0 && $('#seconds').text() == 0) {
					stop()
					document.getElementById(audio).play()
				}
			}, 1000)
		} else {
			clearInterval(timer)
			$('#startStopButton').text('Start')
			timer = null
		}
	})
})
