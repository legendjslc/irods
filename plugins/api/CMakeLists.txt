find_package(OpenSSL REQUIRED)

set(
  IRODS_API_PLUGIN_SOURCES_helloworld_server
  ${CMAKE_SOURCE_DIR}/plugins/api/src/helloworld.cpp
  )

set(
  IRODS_API_PLUGIN_SOURCES_helloworld_client
  ${CMAKE_SOURCE_DIR}/plugins/api/src/helloworld.cpp
  )

set(
  IRODS_API_PLUGIN_COMPILE_DEFINITIONS_helloworld_server
  RODS_SERVER
  ENABLE_RE
  )

set(
  IRODS_API_PLUGIN_COMPILE_DEFINITIONS_helloworld_client
  )

set(
  IRODS_API_PLUGIN_LINK_LIBRARIES_helloworld_server
  irods_server
  )

set(
  IRODS_API_PLUGIN_LINK_LIBRARIES_helloworld_client
  irods_client
  )

set(
  IRODS_API_PLUGINS
  helloworld_server
  helloworld_client
  )

foreach(PLUGIN ${IRODS_API_PLUGINS})
  add_library(
    ${PLUGIN}
    MODULE
    ${IRODS_API_PLUGIN_SOURCES_${PLUGIN}}
    )

  target_include_directories(
    ${PLUGIN}
    PRIVATE
    ${CMAKE_BINARY_DIR}/lib/core/include
    ${CMAKE_SOURCE_DIR}/lib/core/include
    ${CMAKE_SOURCE_DIR}/lib/api/include
    ${CMAKE_SOURCE_DIR}/server/drivers/include
    ${CMAKE_SOURCE_DIR}/server/core/include
    ${CMAKE_SOURCE_DIR}/server/icat/include
    ${CMAKE_SOURCE_DIR}/server/re/include
    ${IRODS_EXTERNALS_FULLPATH_BOOST}/include
    ${IRODS_EXTERNALS_FULLPATH_JANSSON}/include
    ${IRODS_EXTERNALS_FULLPATH_ARCHIVE}/include
    )

  target_link_libraries(
    ${PLUGIN}
    PRIVATE
    ${IRODS_API_PLUGIN_LINK_LIBRARIES_${PLUGIN}}
    irods_plugin_dependencies
    irods_common
    ${IRODS_EXTERNALS_FULLPATH_BOOST}/lib/libboost_filesystem.so
    ${IRODS_EXTERNALS_FULLPATH_BOOST}/lib/libboost_system.so
    ${IRODS_EXTERNALS_FULLPATH_ARCHIVE}/lib/libarchive.so
    ${OPENSSL_CRYPTO_LIBRARY}
    )

  target_compile_definitions(${PLUGIN} PRIVATE ${IRODS_API_PLUGIN_COMPILE_DEFINITIONS_${PLUGIN}} ${IRODS_COMPILE_DEFINITIONS} BOOST_SYSTEM_NO_DEPRECATED)
  target_compile_options(${PLUGIN} PRIVATE -Wno-write-strings)
  set_property(TARGET ${PLUGIN} PROPERTY CXX_STANDARD ${IRODS_CXX_STANDARD})
endforeach()

install(
  TARGETS
    ${IRODS_API_PLUGINS}
  LIBRARY
    DESTINATION ${IRODS_HOME_DIRECTORY}/plugins/api
    COMPONENT ${IRODS_PACKAGE_COMPONENT_SERVER_NAME}
  )
