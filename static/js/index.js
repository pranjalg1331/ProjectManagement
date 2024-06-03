const body = document.querySelector("body");
const darkLight = document.querySelector("#darkLight");
const sidebar = document.querySelector(".sidebar");
const submenuItems = document.querySelectorAll(".submenu_item");
const sidebarOpen = document.querySelector("#sidebarOpen");
const sidebarClose = document.querySelector(".collapse_sidebar");
const sidebarExpand = document.querySelector(".expand_sidebar");
const Dashboard=document.querySelector(".Dashboard");
sidebarOpen.addEventListener("click", () => sidebar.classList.toggle("close"));
console.log("hello");
sidebarClose.addEventListener("click", () => {
  sidebar.classList.add("close", "hoverable");
  Dashboard.classList.add("dash-ex");
});
sidebarExpand.addEventListener("click", () => {
  sidebar.classList.remove("close", "hoverable");
  Dashboard.classList.remove("dash-ex");
});

sidebar.addEventListener("mouseenter", () => {
  if (sidebar.classList.contains("hoverable")) {
    sidebar.classList.remove("close");
    Dashboard.classList.remove("dash-ex");
  }
});
sidebar.addEventListener("mouseleave", () => {
  if (sidebar.classList.contains("hoverable")) {
    sidebar.classList.add("close");
    Dashboard.classList.add("dash-ex");
  }
});


submenuItems.forEach((item, index) => {
  item.addEventListener("click", () => {
    item.classList.toggle("show_submenu");
    submenuItems.forEach((item2, index2) => {
      if (index !== index2) {
        item2.classList.remove("show_submenu");
      }
    });
  });
});

if (window.innerWidth < 768) {
  sidebar.classList.add("close");
} else {
  sidebar.classList.remove("close");
}


function markcomplete(taskId) {
  $.ajax({
      type: 'POST',
      url: '/mark_task_completed/',  // URL to your Django view
      data: {
          task_id: taskId,

      },
      success: function(data) {
          if (data.success) {
              
              setTimeout(function() {
                  location.reload();
              }, 500); // Reload after 1 second (1000 milliseconds)
          } else {
              alert('Failed to mark task as completed.');
          }
      },
      error: function(xhr, status, error) {
          console.error('Error marking task as completed:', error);
      }
  });
}

function markincomplete(taskId) {
  $.ajax({
      type: 'POST',
      url: '/mark_task_incompleted/',  // URL to your Django view
      data: {
          task_id: taskId,

      },
      success: function(data) {
          if (data.success) {
              
              setTimeout(function() {
                  location.reload();
              }, 500); // Reload after 1 second (1000 milliseconds)
          } else {
              alert('Failed to mark task as incompleted.');
          }
      },
      error: function(xhr, status, error) {
          console.error('Error marking task as incompleted:', error);
      }
  });
}

function deleteTask(taskId) {
  $.ajax({
      type: 'POST',
      url: '/deleteTask/',  // URL to your Django view
      data: {
          task_id: taskId,

      },
      success: function(data) {
          if (data.success) {
              
              setTimeout(function() {
                  location.reload();
              }, 500); // Reload after 1 second (1000 milliseconds)
          } else {
              alert('Failed to delete task.');
          }
      },
      error: function(xhr, status, error) {
          console.error('Error deleting task:', error);
      }
  });
}