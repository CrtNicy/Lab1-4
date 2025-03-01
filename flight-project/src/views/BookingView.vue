<script setup lang="ts">
import { reactive, ref } from 'vue';
import { RouterLink, RouterView } from 'vue-router'
import { useRouter } from 'vue-router';
import { useStore } from 'vuex'
// import HelloWorld from './components/HelloWorld.vue'
import axios from 'axios'
import type { Store } from 'element-plus/es/components/table/src/store';
import { ElMessage } from 'element-plus';

const router = useRouter()
const store = useStore()

interface Booking {
  flight_number: string,
  flight_type: string,
  departure_time: Date,
  passenger: string
}
const deleteDialogVisible = ref(false)
const addDialogVisible = ref(false)
const deleteId = ref(0)
const bookingData: Booking[] = reactive([])
const addInfo = reactive({
  passenger: {
    username: store.state.username
  },
  seat_number: '',
  flight: null,
})

// 添加编辑对话框的状态和数据
const editDialogVisible = ref(false)
const editInfo = reactive({
  id: null as number | null,
  seat_number: '',
  flight_number: ''
})

const loadBookings = () => {
  axios.get('http://127.0.0.1:8000/app/api/bookings/')
    .then(response => {
      const userBookings = response.data.filter(
        (booking: any) => booking.passenger.username === store.state.username
      );
      bookingData.splice(0, bookingData.length);
      userBookings.forEach((booking: any) => {
        axios.get('http://127.0.0.1:8000/app/api/flights/' + booking.flight)
          .then(flightResponse => {
            const bookingInfo: Booking = {
              flight_number: flightResponse.data.flight_number,
              flight_type: flightResponse.data.flight_type,
              departure_time: new Date(flightResponse.data.departure_time),
              passenger: store.state.username
            };
            bookingData.push(bookingInfo);
          })
          .catch(error => {
            console.error(error);
          });
      });
    })
    .catch(error => {
      console.error(error);
    });
};

// 页面加载时获取数据
loadBookings();

const handleAdd = (e: any) => {
  // 先检查航班是否存在
  axios.get('http://127.0.0.1:8000/app/api/flights/')
    .then(response => {
      console.log('所有航班:', response.data);
      const flight = response.data.find((f: any) => f.flight_number === addInfo.flight);
      if (!flight) {
        ElMessage({
          type: 'error',
          message: '航班号不存在',
          duration: 2000
        });
        return;
      }
      console.log('找到航班:', flight);

      // 检查用户是否已经预订了这个航班
      axios.get('http://127.0.0.1:8000/app/api/bookings/')
        .then(bookingResponse => {
          console.log('所有预订:', bookingResponse.data);
          const existingBooking = bookingResponse.data.find(
            (b: any) => b.passenger.username === store.state.username && b.flight === flight.id
          );

          if (existingBooking) {
            ElMessage({
              type: 'error',
              message: '您已经预订过这个航班',
              duration: 2000
            });
            return;
          }

          // 创建预订
          const bookingData = {
            passenger_id: store.state.id,  // 使用passenger_id而不是passenger
            seat_number: addInfo.seat_number,
            flight: flight.id
          };
          console.log('发送预订数据:', bookingData);
          console.log('当前用户信息:', {
            id: store.state.id,
            username: store.state.username,
            bookings: store.state.bookings
          });

          axios.post('http://127.0.0.1:8000/app/api/bookings/', bookingData)
            .then(response => {
              console.log('预订成功响应:', response.data);
              ElMessage({
                type: 'success',
                message: '预订成功',
                duration: 2000
              });
              
              // 重新加载预订列表
              loadBookings();
              addDialogVisible.value = false;
              
              // 清空表单
              addInfo.flight = null;
              addInfo.seat_number = '';
            })
            .catch(error => {
              console.error('预订错误:', error);
              console.error('错误响应:', error.response);
              console.error('错误数据:', error.response?.data);
              ElMessage({
                type: 'error',
                message: '预订失败：' + (error.response?.data?.detail || error.message || '未知错误'),
                duration: 2000
              });
            });
        })
        .catch(error => {
          console.error('获取预订列表错误:', error);
          console.error('错误响应:', error.response);
          ElMessage({
            type: 'error',
            message: '获取预订信息失败',
            duration: 2000
          });
        });
    })
    .catch(error => {
      console.error('获取航班列表错误:', error);
      console.error('错误响应:', error.response);
      ElMessage({
        type: 'error',
        message: '获取航班信息失败',
        duration: 2000
      });
    });
};

const handleEdit = (index: number) => {
  const booking = bookingData[index];
  // 获取完整的预订信息
  axios.get('http://127.0.0.1:8000/app/api/bookings/')
    .then(response => {
      console.log('所有预订:', response.data);
      console.log('当前预订:', booking);
      
      // 先获取航班信息
      axios.get('http://127.0.0.1:8000/app/api/flights/')
        .then(flightResponse => {
          const flight = flightResponse.data.find((f: any) => f.flight_number === booking.flight_number);
          if (!flight) {
            ElMessage({
              type: 'error',
              message: '未找到航班信息',
              duration: 2000
            });
            return;
          }
          
          const userBooking = response.data.find(
            (b: any) => b.passenger.username === store.state.username && 
                      b.flight === flight.id
          );
          
          console.log('找到的预订:', userBooking);
          
          if (userBooking) {
            editInfo.id = userBooking.id;
            editInfo.seat_number = userBooking.seat_number;
            editInfo.flight_number = booking.flight_number;
            editDialogVisible.value = true;
          } else {
            ElMessage({
              type: 'error',
              message: '未找到对应的预订记录',
              duration: 2000
            });
          }
        })
        .catch(error => {
          console.error('获取航班信息失败:', error);
          ElMessage({
            type: 'error',
            message: '获取航班信息失败',
            duration: 2000
          });
        });
    })
    .catch(error => {
      console.error('获取预订信息失败:', error);
      ElMessage({
        type: 'error',
        message: '获取预订信息失败',
        duration: 2000
      });
    });
};

const handleEditSubmit = () => {
  if (!editInfo.id) return;
  
  // 更新预订信息
  axios.patch(`http://127.0.0.1:8000/app/api/bookings/${editInfo.id}/`, {
    seat_number: editInfo.seat_number
  })
    .then(response => {
      ElMessage({
        type: 'success',
        message: '更新成功',
        duration: 2000
      });
      loadBookings(); // 重新加载预订列表
      editDialogVisible.value = false;
    })
    .catch(error => {
      console.error('更新失败:', error);
      ElMessage({
        type: 'error',
        message: '更新失败：' + (error.response?.data?.detail || error.message || '未知错误'),
        duration: 2000
      });
    });
};

const handleDelete = () => {
  if (deleteId.value === null) return;
  
  const booking = bookingData[deleteId.value];
  // 获取完整的预订信息
  axios.get('http://127.0.0.1:8000/app/api/bookings/')
    .then(response => {
      console.log('所有预订:', response.data);
      console.log('当前预订:', booking);
      
      // 先获取航班信息
      axios.get('http://127.0.0.1:8000/app/api/flights/')
        .then(flightResponse => {
          const flight = flightResponse.data.find((f: any) => f.flight_number === booking.flight_number);
          if (!flight) {
            ElMessage({
              type: 'error',
              message: '未找到航班信息',
              duration: 2000
            });
            return;
          }
          
          const userBooking = response.data.find(
            (b: any) => b.passenger.username === store.state.username && 
                      b.flight === flight.id
          );
          
          console.log('找到的预订:', userBooking);
          
          if (userBooking) {
            axios.delete('http://127.0.0.1:8000/app/api/bookings/' + userBooking.id)
              .then(response => {
                bookingData.splice(deleteId.value, 1);
                ElMessage({
                  type: 'success',
                  message: '删除成功',
                  duration: 2000
                });
                deleteDialogVisible.value = false;
              })
              .catch(error => {
                console.error('删除失败:', error);
                ElMessage({
                  type: 'error',
                  message: '删除失败：' + (error.response?.data?.detail || error.message || '未知错误'),
                  duration: 2000
                });
              });
          } else {
            ElMessage({
              type: 'error',
              message: '未找到对应的预订记录',
              duration: 2000
            });
          }
        })
        .catch(error => {
          console.error('获取航班信息失败:', error);
          ElMessage({
            type: 'error',
            message: '获取航班信息失败',
            duration: 2000
          });
        });
    })
    .catch(error => {
      console.error('获取预订列表失败:', error);
      ElMessage({
        type: 'error',
        message: '获取预订信息失败',
        duration: 2000
      });
    });
};

// 添加表单验证规则
const rules = {
  flight: [
    { required: true, message: '请输入航班号', trigger: 'blur' },
    { min: 3, max: 10, message: '航班号长度应为3-10个字符', trigger: 'blur' }
  ],
  seat_number: [
    { required: true, message: '请输入座位号', trigger: 'blur' },
    { pattern: /^[A-Z]?[0-9]+$/, message: '座位号格式不正确', trigger: 'blur' }
  ]
};

// 添加确认删除方法
const confirmDelete = (index: number) => {
  deleteId.value = index;
  deleteDialogVisible.value = true;
};

</script>

<template>
  <div class="booking">
    <div class="header">
      <h2><i class="el-icon-ticket"></i> 我的机票预订</h2>
      <el-button type="primary" size="large" icon="el-icon-plus" @click="addDialogVisible = true">
        预订新机票
      </el-button>
    </div>

    <!-- 统计信息卡片 -->
    <div class="statistics">
      <el-row :gutter="20">
        <el-col :span="8">
          <el-card shadow="hover">
            <template #header>
              <div class="card-header">
                <i class="el-icon-tickets"></i>
                <span>总预订数</span>
              </div>
            </template>
            <div class="card-content">
              {{ bookingData.length }}
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card shadow="hover">
            <template #header>
              <div class="card-header">
                <i class="el-icon-user"></i>
                <span>当前用户</span>
              </div>
            </template>
            <div class="card-content">
              {{ store.state.username }}
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card shadow="hover">
            <template #header>
              <div class="card-header">
                <i class="el-icon-date"></i>
                <span>最近预订</span>
              </div>
            </template>
            <div class="card-content">
              {{ bookingData.length > 0 ? bookingData[bookingData.length - 1].flight_number : '无' }}
            </div>
          </el-card>
        </el-col>
      </el-row>
    </div>

    <!-- 预订列表表格 -->
    <el-card class="booking-table">
      <template #header>
        <div class="card-header">
          <span>预订列表</span>
          <el-button type="primary" plain size="small" @click="loadBookings">
            <i class="el-icon-refresh"></i> 刷新
          </el-button>
        </div>
      </template>
      <el-table :data="bookingData" border stripe style="width: 100%">
        <el-table-column prop="flight_number" label="航班编号">
          <template #default="scope">
            <el-tag>{{ scope.row.flight_number }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="flight_type" label="航班类型">
          <template #default="scope">
            <el-tag :type="scope.row.flight_type === 'ARR' ? 'success' : 'warning'">
              {{ scope.row.flight_type === 'ARR' ? '到达' : '出发' }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="departure_time" label="出发时间">
          <template #default="scope">
            <i class="el-icon-time"></i>
            {{ new Date(scope.row.departure_time).toLocaleString() }}
          </template>
        </el-table-column>
        <el-table-column prop="passenger" label="乘客">
          <template #default="scope">
            <el-avatar size="small">{{ scope.row.passenger.charAt(0).toUpperCase() }}</el-avatar>
            {{ scope.row.passenger }}
          </template>
        </el-table-column>
        <el-table-column fixed="right" label="操作" width="150">
          <template #default="scope">
            <el-button-group>
              <el-button type="primary" size="small" icon="el-icon-edit" @click="handleEdit(scope.$index)">
                编辑
              </el-button>
              <el-button type="danger" size="small" icon="el-icon-delete" @click="confirmDelete(scope.$index)">
                退订
              </el-button>
            </el-button-group>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
  </div>

  <!-- 删除确认对话框 -->
  <el-dialog
    v-model="deleteDialogVisible"
    title="确认退订"
    width="30%"
    destroy-on-close
    center
  >
    <div class="delete-confirm">
      <i class="el-icon-warning" style="color: #E6A23C; font-size: 24px;"></i>
      <p>确定要退订该航班吗？此操作不可恢复。</p>
    </div>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="deleteDialogVisible = false">取消</el-button>
        <el-button type="danger" @click="handleDelete">确定退订</el-button>
      </span>
    </template>
  </el-dialog>

  <!-- 添加预订对话框 -->
  <el-dialog
    width="40%"
    v-model="addDialogVisible"
    title="预订新机票"
    destroy-on-close
  >
    <el-form
      ref="ruleFormRef"
      :model="addInfo"
      :rules="rules"
      label-width="100px"
      status-icon
    >
      <el-form-item label="航班号" prop="flight" required>
        <el-input
          v-model="addInfo.flight"
          placeholder="请输入航班号"
          prefix-icon="el-icon-plane"
        />
      </el-form-item>
      <el-form-item label="座位号" prop="seat_number" required>
        <el-input
          v-model="addInfo.seat_number"
          placeholder="请输入座位号"
          prefix-icon="el-icon-seat"
        />
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="addDialogVisible = false">取消</el-button>
        <el-button type="primary" @click="handleAdd">确认预订</el-button>
      </span>
    </template>
  </el-dialog>

  <!-- 添加编辑对话框 -->
  <el-dialog
    width="40%"
    v-model="editDialogVisible"
    title="编辑预订"
    destroy-on-close
  >
    <el-form
      ref="editFormRef"
      :model="editInfo"
      :rules="rules"
      label-width="100px"
      status-icon
    >
      <el-form-item label="航班号" required>
        <el-input
          v-model="editInfo.flight_number"
          disabled
          prefix-icon="el-icon-plane"
        />
      </el-form-item>
      <el-form-item label="座位号" prop="seat_number" required>
        <el-input
          v-model="editInfo.seat_number"
          placeholder="请输入新的座位号"
          prefix-icon="el-icon-seat"
        />
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="editDialogVisible = false">取消</el-button>
        <el-button type="primary" @click="handleEditSubmit">确认修改</el-button>
      </span>
    </template>
  </el-dialog>
</template>

<style scoped>
.booking {
  padding: 20px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.header h2 {
  margin: 0;
  color: #303133;
}

.statistics {
  margin-bottom: 20px;
}

.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.card-header i {
  margin-right: 8px;
  font-size: 18px;
}

.card-content {
  font-size: 24px;
  font-weight: bold;
  text-align: center;
  color: #409EFF;
}

.booking-table {
  margin-top: 20px;
}

.delete-confirm {
  text-align: center;
  padding: 20px 0;
}

.delete-confirm i {
  margin-bottom: 10px;
}

.delete-confirm p {
  margin: 0;
  color: #606266;
}

.el-button-group {
  display: flex;
  gap: 8px;
}
</style>
