set(
  IRODS_MICROSERVICE_ADMINISTRATION_PLUGINS
  msisync_to_archive
  msi_update_unixfilesystem_resource_free_space
  )

foreach(PLUGIN ${IRODS_MICROSERVICE_ADMINISTRATION_PLUGINS})
  add_library(
    ${PLUGIN}
    MODULE
    ${CMAKE_SOURCE_DIR}/plugins/microservices/administration/${PLUGIN}/lib${PLUGIN}.cpp
    )

  target_include_directories(
    ${PLUGIN}
    PRIVATE
    ${CMAKE_BINARY_DIR}/lib/core/include
    ${CMAKE_SOURCE_DIR}/lib/core/include
    ${CMAKE_SOURCE_DIR}/lib/api/include
    ${CMAKE_SOURCE_DIR}/server/drivers/include
    ${CMAKE_SOURCE_DIR}/server/api/include
    ${CMAKE_SOURCE_DIR}/server/core/include
    ${CMAKE_SOURCE_DIR}/server/icat/include
    ${CMAKE_SOURCE_DIR}/server/re/include
    ${IRODS_EXTERNALS_FULLPATH_BOOST}/include
    ${IRODS_EXTERNALS_FULLPATH_JANSSON}/include
    ${CURL_INCLUDE_DIRS}
    )

  target_link_libraries(
    ${PLUGIN}
    PRIVATE
    irods_server
    irods_common
    ${IRODS_EXTERNALS_FULLPATH_BOOST}/lib/libboost_filesystem.so
    ${IRODS_EXTERNALS_FULLPATH_BOOST}/lib/libboost_system.so
    ${IRODS_EXTERNALS_FULLPATH_JANSSON}/lib/libjansson.so
    ${CURL_LIBRARIES}
    )

  target_compile_definitions(${PLUGIN} PRIVATE ENABLE_RE ${IRODS_COMPILE_DEFINITIONS} BOOST_SYSTEM_NO_DEPRECATED)
  target_compile_options(${PLUGIN} PRIVATE -Wno-write-strings)
  set_property(TARGET ${PLUGIN} PROPERTY CXX_STANDARD ${IRODS_CXX_STANDARD})
endforeach()

install(
  TARGETS
    ${IRODS_MICROSERVICE_ADMINISTRATION_PLUGINS}
  LIBRARY
    DESTINATION ${IRODS_HOME_DIRECTORY}/plugins/microservices
    COMPONENT ${IRODS_PACKAGE_COMPONENT_SERVER_NAME}
  )
