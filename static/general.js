container = document.getElementById('change-password')
containerCover = container.querySelector('.add-form-cover')

function showChangePassword(){
	container.style.display = 'flex';
	container.style.opacity = 1
}

containerCover.addEventListener('click', event => {
	container.style.display = 'none';
	container.style.opacity = 0
})