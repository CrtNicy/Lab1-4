<script setup lang="ts">

</script>

<template>
  <div class="home">
    <el-row justify="center" :gutter="50" style="padding: 100px;">
      <el-col :span="4">
        <h3 class="mb-2" style="text-align: center">航班信息系统</h3>
        <el-menu active-text-color="#ffd04b" background-color="#545c64" class="el-menu-vertical-demo" default-active="1"
          text-color="#fff" router>
          <el-menu-item index="1" route="booking">
            <el-icon>
              <MessageBox />
            </el-icon>
            <span>预订信息</span>
          </el-menu-item>
          <el-menu-item index="2" route="flight">
            <el-icon>
              <setting />
            </el-icon>
            <span>航班信息</span>
          </el-menu-item>
        </el-menu>
      </el-col>
      <el-col :span="15">
        <RouterView />
      </el-col>
    </el-row>
  </div>
</template>

<style scoped></style>