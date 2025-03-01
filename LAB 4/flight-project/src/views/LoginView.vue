<script setup lang="ts">
import { reactive, ref } from 'vue';
import { RouterLink, RouterView } from 'vue-router'
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';
import { ElMessage } from 'element-plus';
// import HelloWorld from './components/HelloWorld.vue'
import axios from 'axios'

const router = useRouter()
const store = useStore()

const loginInfo = reactive({
  username: '',
  password: ''
})
const addInfo = reactive({
  username: '',
  password: '',
  repassword: '',
})



const showAddDialog = ref(false)

const handleLogin = () => {
  axios.post('http://127.0.0.1:8000/app/api/login/', {
    username: loginInfo.username,
    password: loginInfo.password
  })
    .then(response => {
      console.log(response);
      store.state.id = response.data.id
      store.state.username = response.data.username
      store.state.password = response.data.password
      store.state.bookings = response.data.bookings
      console.log(store.state.bookings);

      ElMessage({
        type: 'success',
        message: '登录成功',
        duration: 2000 // 显示时间 2s
      });

      router.push({
        name: 'booking',
      })
      // RouterView.
    })
    .catch(error => {
      ElMessage({
        type: 'error',
        message: '登录失败',
        duration: 2000 // 显示时间 2s
      });
    });

}
const handleAdd = () => {
  if (addInfo.repassword != addInfo.password) {
    ElMessage({
      type: 'error',
      message: '两次输入的密码不匹配，请重新输入',
      duration: 2000 // 显示时间 2s
    });
    return;
  }
  axios.post('http://127.0.0.1:8000/app/api/passengers/', {
    username: addInfo.username,
    password: addInfo.password
  })
    .then(response => {
      ElMessage({
        type: 'success',
        message: '注册成功',
        duration: 2000 // 显示时间 2s
      });
    })
    .catch(error => {
      ElMessage({
        type: 'error',
        message: '注册失败',
        duration: 2000 // 显示时间 2s
      });
    });
  showAddDialog.value = false
}

</script>

<template>
  <div class="login">
    <el-card class="login-card">
      <h2>登录</h2>
      <div class="card-input">
        <el-input size="large" v-model="loginInfo.username" class="w-50 m-2" placeholder="请输入账号" />
      </div>
      <div class="card-input">
        <el-input type="password" size="large" v-model="loginInfo.password" class="w-50 m-2" placeholder="请输入密码" />
      </div>
      <div class="card-button">
        <el-button @click="showAddDialog = true">注册</el-button>
        <el-button type="primary" @click="handleLogin">登录</el-button>
      </div>
    </el-card>
    <el-dialog width="30%" v-model="showAddDialog" title="账号注册">
      <el-form ref="ruleFormRef" :model="addInfo" label-width="auto">
        <el-form-item label="账号" prop="username">
          <el-input v-model="addInfo.username" placeholder="请输入用户账号" />
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password" v-model="addInfo.password" placeholder="请输入用户密码" />
        </el-form-item>
        <el-form-item label="确认密码" prop="repassword">
          <el-input type="password" v-model="addInfo.repassword" placeholder="再次输入密码" />
        </el-form-item>
      </el-form>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="showAddDialog = false">取消</el-button>
          <el-button type="primary" @click="handleAdd">添加</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<style scoped>
.login {
  width: 100%;
  text-align: center;
  line-height: 40px;
}

.login-card {
  width: 20%;
  margin: 100px auto;
}

.card-input {
  margin-top: 30px;
}

.card-button {
  margin-top: 30px;
}
</style>
