const birthDateInput = document.getElementById('id_birth_date');
const updateDateInput = document.getElementById('id_update_date');
const dateInput = document.getElementById('id_date');
const followUpDateInput = document.getElementById('id_follow_up_date');

const pickerDI = MCDatepicker.create({
  el: '#id_date',
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date(),
});

const pickerBD = MCDatepicker.create({
  el: '#id_birth_date',
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date(),
});

const pickerUD = MCDatepicker.create({
  el: '#id_update_date',
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date(),
});

const pickerFUD = MCDatepicker.create({
  el: '#id_follow_up_date',
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date(),
});

birthDateInput.addEventListener("click", (evt) => {
  pickerBD.open();
});

updateDateInput.addEventListener("click", (evt) => {
  pickerUD.open();
});

dateInput.addEventListener("click", (evt) => {
  pickerDI.open();
});

followUpDateInput.addEventListener("click", (evt) => {
  pickerDI.open();
});
