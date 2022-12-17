let form = document.getElementById('add-form')
let form_cover = document.querySelector('#add-form .add-form-cover')


form_cover.addEventListener('click', event => {
	form.style.display = 'none'
	form.style.opacity = 0

	form.querySelectorAll('.add-form-user-roles small').forEach(item => item.remove())
})

function userCard(card){
	form.style.display = 'flex'
	form.style.opacity = 1

	form.querySelector('.add-category-form').setAttribute(
		'action',
		`${window.location.origin}/users/update/${card.querySelector('.user-id').innerText}`
	)

	form.querySelector('#name').value = card.querySelector('.user-first-name').innerText
	form.querySelector('#role').value = card.querySelector('.user-role').innerText
}


function feeCard(card){
	form.style.display = 'flex'
	form.style.opacity = 1
	form.querySelector('.add-category-form').setAttribute('action', `${window.location.origin}/fees/update`)

	form.querySelector('#price').value = card.querySelector('.fee-price').innerText
	form.querySelector('#payment').value = card.querySelector('.fee-payment').innerText
	form.querySelector('#distance').value = card.querySelector('.fee-distance').innerText
	form.querySelector('#nonpaid').value = card.querySelector('.fee-nonpaid').innerText
}