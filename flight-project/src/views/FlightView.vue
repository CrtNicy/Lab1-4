<script setup lang="ts">
import { reactive, ref } from 'vue';
import { RouterLink, RouterView } from 'vue-router'
import { useRouter } from 'vue-router';
import { useStore } from 'vuex'
// import HelloWorld from './components/HelloWorld.vue'
import axios from 'axios'
import type { Store } from 'element-plus/es/components/table/src/store';
import { ElMessage } from 'element-plus';

interface Flight {
  id: number,
  flight_number: string,
  airline: string,
  departure_time: Date,
  arrive_time: Date,
  flight_type: string,
  gate_number: string,
}
const router = useRouter()
const store = useStore()
const watchDialogVisible = ref(false)
const deleteId = ref(0)
const textarea2 = ref('')
const rateStar = ref(0)
interface Flight {
  id: number,
  flight_number: string,
  airline: string,
  departure_time: Date,
  arrive_time: Date,
  flight_type: string,
  gate_number: string,
}
const watchInfo = reactive({
  id: 0,
  flight_number: '',
  airline: '',
  flight_type: '',
  gate_number: '',
})

const flightData: Flight[] = reactive([])

const mockData = reactive([
  {
    id: 1,
    comment_text: '哇这个航班确实可以啊',
    rating: 8,
    commenter_name: 'jason',
    comment_date: '2023/3/11',
    flight: 1,
  },
  {
    id: 1,
    comment_text: '体验很好下次还要坐你的飞机',
    rating: 6,
    commenter_name: 'jason',
    comment_date: '2023/3/12',
    flight: 1,
  },
  {
    id: 1,
    comment_text: '哇这个航班确实可以啊',
    rating: 5,
    commenter_name: 'jason',
    comment_date: '2023/3/15',
    flight: 1,
  },
])

const handleWatch = (index: number, row: any) => {
  watchDialogVisible.value = true;
  axios.get('http://127.0.0.1:8000/app/api/flights/' + row.id, {
  })
    .then(response => {
      watchInfo.id = response.data.id;
      watchInfo.flight_number = response.data.flight_number;
      watchInfo.airline = response.data.airline;
      watchInfo.flight_type = response.data.flight_type;
      watchInfo.gate_number = response.data.gate_number;
      loadComments(response.data.id);
    })
    .catch(error => {
      console.error(error);
    });
}

const handleComment = () => {
  const now = new Date()
  const dateString = now.toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit'
  }).replace(/\//g, '/');
  
  axios.post('http://127.0.0.1:8000/app/api/comments/', {
    comment_text: textarea2.value,
    rating: rateStar.value,
    commenter_name: store.state.username,
    comment_date: dateString,
    flight: watchInfo.id
  })
    .then(response => {
      mockData.push(response.data);
      ElMessage({
        type: 'success',
        message: '评论成功',
        duration: 2000
      });
      textarea2.value = '';
      rateStar.value = 0;
    })
    .catch(error => {
      console.error(error);
      ElMessage({
        type: 'error',
        message: '评论失败',
        duration: 2000
      });
    });
}

// 获取评论列表
const loadComments = (flightId: number) => {
  axios.get(`http://127.0.0.1:8000/app/api/comments/?flight=${flightId}`)
    .then(response => {
      mockData.splice(0, mockData.length, ...response.data);
    })
    .catch(error => {
      console.error(error);
    });
}

axios.get('http://127.0.0.1:8000/app/api/flights/', {
})
  .then(response => {
    flightData.splice(0, flightData.length, ...response.data)
  })
  .catch(error => {
    console.error(error);
  });


</script>

<template>
  <div class="flight">
    <el-table :data="flightData" border stripe style="width: 100%">
      <el-table-column prop="id" label="航班编号" />
      <el-table-column prop="flight_number" label="航班号" />
      <el-table-column prop="departure_time" label="出发时间" />
      <el-table-column prop="arrival_time" label="到达时间" />
      <el-table-column prop="flight_type" label="航班类型" />
      <el-table-column prop="gate_number" label="登机口" />
      <el-table-column fixed="right" label="操作">
        <template #default="scope">
          <el-button link type="primary" size="small" @click="handleWatch(scope.$index, scope.row)">查看</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog width="30%" v-model="watchDialogVisible" title="查看航班">
      <el-form ref="ruleFormRef" :model="watchInfo" label-width="auto">
        <el-form-item label="航班编号" prop="id">
          <el-input disabled v-model="watchInfo.id" placeholder="航班编号" />
        </el-form-item>
        <el-form-item label="航班号" prop="flight_number">
          <el-input disabled v-model="watchInfo.flight_number" placeholder="航班号" />
        </el-form-item>
        <el-form-item label="航线" prop="airline">
          <el-input disabled v-model="watchInfo.airline" placeholder="航线" />
        </el-form-item>
        <el-form-item label="航班类型" prop="flight_type">
          <el-input disabled v-model="watchInfo.flight_type" placeholder="航班类型" />
        </el-form-item>
        <el-form-item label="登机口" prop="flight">
          <el-input disabled v-model="watchInfo.gate_number" placeholder="登机口" />
        </el-form-item>
      </el-form>
      <el-collapse>
        <el-collapse-item title="评论区" name="1">
          <el-timeline>
            <el-timeline-item v-for="item in mockData" :timestamp="item.comment_date" placement="top">
              <el-card>
                <div style="display: flex;">
                  <h3>用户：{{ item.commenter_name }}</h3>
                  <h4 style="margin-left: 30px;">评分: {{ item.rating }}分</h4>
                </div>
                <p>{{ item.comment_text }}</p>
              </el-card>
            </el-timeline-item>
          </el-timeline>
          <el-input v-model="textarea2" :autosize="{ minRows: 2, maxRows: 4 }" type="textarea"
            placeholder="Please input" />
          <el-rate v-model="rateStar" />
          <el-button @click="handleComment">发表评论</el-button>
        </el-collapse-item>
      </el-collapse>


      <template #footer>
        <span class="dialog-footer">
          <el-button @click="watchDialogVisible = false">关闭</el-button>
          <!-- <el-button type="primary" @click="handleAdd">添加</el-button> -->
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<style scoped></style>